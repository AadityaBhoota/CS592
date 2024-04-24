import json
import re
from typing import List
import anthropic

import openai
from dataset import load_dataset, load_humaneval_dataset, load_mbpp_sanitized_dataset
from execution import execute_code
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from anthropic import AsyncAnthropic
import os
import time
from pathlib import Path
import backoff
load_dotenv()

openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
anthropic_client = AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
system_prompt = "You are a Python expert, who is tasked with a few problems. Please solve this problem."

ct = 0
dataset_len = 0


@backoff.on_exception(backoff.expo, openai.RateLimitError)
@backoff.on_exception(backoff.expo, openai.InternalServerError)
async def prompt_openai(prompt: str, kidx=0):
    completion = await openai_client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1
    )
    # postprocess code sols to include the only code
    sol = completion.choices[0].message.content
    try:
        idx = sol.index("```python\n")
        code_sol = sol[idx + len("```python\n"):sol.index("```", idx + 1)]
    except:
        # not wrapped ```python, maybe the entire output is the code
        code_sol = sol
    # remove outer level print statements
    code_sol = re.sub(r"\nprint(.)*", "\n", code_sol)
    print("onto", kidx)
    return code_sol


@backoff.on_exception(backoff.expo, anthropic.RateLimitError)
@backoff.on_exception(backoff.expo, anthropic.InternalServerError)
async def prompt_anthropic(prompt: str, kidx=0):
    completion = await anthropic_client.messages.create(
        model="claude-3-haiku-20240307",
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=4096
    )
    # postprocess code sols to include the only code
    sol = completion.content[0].text
    try:
        idx = sol.index("```python\n")
        code_sol = sol[idx + len("```python\n"):sol.index("```", idx + 1)]
    except:
        # not wrapped ```python, maybe the entire output is the code
        code_sol = sol
    # remove outer level print statements
    code_sol = re.sub(r"\nprint(.)*", "\n", code_sol)
    print("onto", kidx)
    return code_sol


async def prompt_k(prompt: str, model: str, k=3):
    if model == "openai":
        api_calls = [prompt_openai(prompt, idx) for idx in range(k)]
    else:
        api_calls = [prompt_anthropic(prompt, idx) for idx in range(k)]
    code_sols = await asyncio.gather(*api_calls)
    global ct
    ct += 1
    print(f"Got: {ct} / {dataset_len}")
    return code_sols


async def batch_prompt(prompts: List[str], model: str, k=3) -> List[List[str]]:
    api_calls = [prompt_k(prompt, model, k) for prompt in prompts]
    code_sols = await asyncio.gather(*api_calls)
    return code_sols


async def experiment(dataset, results_dir: str, experiment_name: str, model: str, k=10, batch_size=5, load_from_file=False):
    # create results dir if not exist
    Path(results_dir).mkdir(parents=True, exist_ok=True)
    test_script_dir = os.path.join(results_dir, "test_scripts")
    Path(test_script_dir).mkdir(parents=True, exist_ok=True)

    global dataset_len
    print("Loading dataset...")
    # dataset = load_humaneval_dataset(dataset_path)
    dataset_len = len(dataset)
    prompts = [task["prompt"] for task in dataset]

    if load_from_file:
        print("Loading sols from file...")
        with open(os.path.join(results_dir, "_sols.json"), "r") as f:
            batch_code_sols = json.load(f)
            batch_code_sols = list(batch_code_sols.values())
    else:
        print("Batch prompting...")
        batch_code_sols = []
        for idx in range(0, len(dataset), batch_size):
            sols = await batch_prompt(prompts[idx:idx + batch_size], model, k)
            batch_code_sols += sols
            with open(os.path.join(results_dir, "_sols.json"), "w") as f:
                labeled_code_sols = {}
                for idx, code_sols in enumerate(batch_code_sols):
                    task_id = dataset[idx]["task_id"]
                    labeled_code_sols[task_id] = code_sols
                json.dump(labeled_code_sols, f, indent=4)

    print()
    print("Executing code and testing...")
    pass_k_metrics = [1, 3, 5, 10]
    pass_k_per_task = {}
    for idx, code_sols in enumerate(batch_code_sols):
        task = dataset[idx]
        pass_k = {f"pass@{k_metric}": 0 for k_metric in pass_k_metrics}
        total_correct = 0
        task_id = task["task_id"].replace("/", "-")
        for cidx, code_sol in enumerate(code_sols):
            # create test script and write to file
            test_script = code_sol + "\n" + task["test"] + "\n" + f"check({task['entry_point']})"
            with open(os.path.join(test_script_dir, f"{task_id}_{cidx}.py"), "w") as f:
                f.write(test_script)
            # execute and redirect output to its own file
            outfile = os.path.join(test_script_dir, f"{task_id}_{cidx}.out")
            passed = execute_code(test_script, timeout=10, outfile=outfile)
            if passed:
                total_correct += 1
                for k_metric in pass_k_metrics:
                    if cidx <= k_metric:
                        pass_k[f"pass@{k_metric}"] += 1
        # record the number of correct solutions in the current task
        pass_k["total_correct"] = total_correct
        pass_k_per_task[task["task_id"]] = pass_k
        print(f"Executed: {idx + 1} / {len(dataset)}")

    with open(os.path.join(results_dir, "_pass_k_count_task.json"), "w") as f:
        json.dump(pass_k_per_task, f, indent=4)

    print("===========")
    print("Summary: ", experiment_name)
    print("---------")
    summary = {f"pass@{k_metric}": 0 for k_metric in pass_k_metrics}
    total_correct = 0
    for pass_k in pass_k_per_task.values():
        for k_metric in pass_k_metrics:
            if pass_k[f"pass@{k_metric}"] > 0:
                summary[f"pass@{k_metric}"] += 1
        if pass_k["total_correct"] > 0:
            total_correct += 1
    pass_k["total"] = len(dataset)

    for pass_k, ct in summary.items():
        print(pass_k, ":", ct / len(dataset))
    
    
    with open(os.path.join(results_dir, "_pass_k_summary.json"), "w") as f:
        json.dump(summary, f, indent=4)
    
    
async def main():
    dataset_name = "mbpp"
    model = "anthropic"

    if dataset_name == "humaneval":
        dataset = load_humaneval_dataset("./data/HumanEval.jsonl")
    else:
        dataset = load_mbpp_sanitized_dataset("./data/mbpp-sanitized-examples.json")
    await experiment(
        dataset,
        results_dir=f"./results/no_framework/{model}/{dataset_name}/",
        experiment_name=f"{dataset_name} (no framework) ({model})",
        model=model,
        k=10,
        load_from_file=False
    )

if __name__ == "__main__":
    start_time = time.time()
    print("Starting...")
    # main()
    asyncio.run(main())
    print()
    print ("Total secs:", time.time() - start_time)