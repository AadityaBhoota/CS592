from typing import List
from dataset import load_dataset, load_humaneval_dataset, load_mbpp_sanitized_dataset
from execution import execute_code
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
import time
from pathlib import Path
load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

k = 20
ct = 0
dataset_len = 0

system_prompt = "You are a Python expert, who is tasked with a few problems. Please solve this problem."

async def prompt_openai(prompt: str):
    global ct
    completion = await client.chat.completions.create(
        model=os.getenv("GPT_MODEL"),
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    ct += 1
    print(f"Got: {ct} / {dataset_len}", end="\r")
    return completion.choices[0].message.content

def batch_prompt_openai(prompts: List[str]) -> List[str]:
    loop = asyncio.get_event_loop()
    prompts = [prompt_openai(prompt) for prompt in prompts]
    sols = loop.run_until_complete(asyncio.gather(*prompts))
    loop.close()
    # postprocess code sols
    code_sols = []
    for sol in sols:
        try:
            idx = sol.index("```python\n")
            code_sol = sol[idx + len("```python\n"):sol.index("```", idx + 1)]
            code_sols.append(code_sol)
        except:
            # does not wrap with ```python, most likely just the code output
            code_sols.append(sol)
    return code_sols


def humaneval():
    # create results dir if not exist
    results_dir = "./results/no_framework/humaneval/"
    Path(results_dir).mkdir(parents=True, exist_ok=True)

    global dataset_len
    print("Loading dataset...")
    dataset = load_humaneval_dataset("./data/HumanEval.jsonl")[:3]
    dataset_len = len(dataset)
    prompts = [task["prompt"] for task in dataset]
    print("Batch prompting...")
    code_sols = batch_prompt_openai(prompts)

    print()
    print("Executing code and testing...")
    correct = 0
    for idx, code_sol in enumerate(code_sols):
        task = dataset[idx]
        # write code solution to file
        # create test script to execute
        test_script = code_sol + "\n" + task["test"] + "\n" + f"check({task['entry_point']})"
        with open(os.path.join(results_dir, task["task_id"].replace("/", "-") + ".py"), "w") as f:
            f.write(test_script)
        passed = execute_code(
            test_script,
            outfile=os.path.join(results_dir, task["task_id"].replace("/", "-") + ".txt")
        )
        if passed:
            correct += 1
        print(f"Executed: {idx + 1} / {len(dataset)}, Passed: {passed}")
    print(f"Total correct: {correct} / {len(dataset)}")
    

def mbpp():
    dataset = load_mbpp_sanitized_dataset("./data/mbpp-sanitized-examples.json")

def main():
    humaneval()
    pass

if __name__ == "__main__":
    start_time = time.time()
    print("Starting...")
    main()
    print()
    print ("Total secs:", time.time() - start_time)