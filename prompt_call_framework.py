from openai import OpenAI
from dotenv import load_dotenv
import os
import asyncio
from anthropic import Anthropic
load_dotenv()

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


async def prompt_openai(system_prompt, prompt, logprobs=None, top_logprobs=None, max_tokens=None, num_responses=1):
    completion = await openai_client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system",
             "content": system_prompt},
            {"role": "user",
             "content": prompt}
        ],
        logprobs=logprobs,
        top_logprobs=top_logprobs,
        max_tokens=max_tokens,
        n=num_responses
    )
    return completion


async def prompt_anthropic(system_prompt, prompt, max_tokens=4096, temperature=1.0):
    message = await anthropic_client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=max_tokens,
        temperature=temperature,
        system=system_prompt,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message


async def planning_stage(model, planning_prompts, problem):
    prompt = planning_prompts[1].replace("[[problem]]", problem)
    if model == "openai":
        response = await prompt_openai(planning_prompts[0], prompt)
        plan = response.choices[0].message.content
    elif model == "anthropic":
        response = await prompt_anthropic(planning_prompts[0], prompt)
        plan = response.content

    return plan


async def full_code_generation(model, plan, problem, full_code_generation_prompts):
    prompt = full_code_generation_prompts[1].replace("[[problem]]", problem).replace("[[plan]]", plan)
    if model == "openai":
        response = await prompt_openai(full_code_generation_prompts[0], prompt)
        plan = response.choices[0].message.content
    elif model == "anthropic":
        response = await prompt_anthropic(full_code_generation_prompts[0], prompt)
        plan = response.content

    return plan


# Assumes planning response is in the form of a numbered list with "\n" as the delimiter
def parse_planning_response(planning_response):
    steps = planning_response.split("\n")
    steps = [step.strip() for step in steps if step.strip()]

    return steps


def is_positive(string):
    # Implement after prompts are finished
    return True


# Each prompt parameter consists of a tuple of (system_prompt, prompt)
async def refining_stage(model, planning_steps, step_explaining_prompts, code_generation_prompts, code_checking_prompts, problem_prompt, max_iterations=3):
    prev_steps = []
    prev_code = []
    for planning_step in planning_steps:
        # Explaining check
        explaining_prompt = step_explaining_prompts[1].replace("[[curr_step]]", planning_step).replace("[[problem_prompt]]", problem_prompt)
        if model == "openai":
            response = await prompt_openai(step_explaining_prompts[0], explaining_prompt)
            step_check_result = response.choices[0].messages.content
        elif model == "anthropic":
            response = await prompt_anthropic(step_explaining_prompts[0], explaining_prompt)
            step_check_result = response.content
        if not is_positive(step_check_result):
            # Not sure what to do here
            pass

        # Code generation step
        num_iterations = 0
        while num_iterations < max_iterations:
            code_generation_prompt = code_generation_prompts[1].replace("[[prev_code]]", "\n".join(prev_code)).replace("[[prev_steps]]", "\n".join(prev_steps)).replace("[[problem_prompt]]", problem_prompt).replace("[[curr_step]]", planning_step)
            if model == "openai":
                response = await prompt_openai(code_generation_prompts[1], code_generation_prompt)
                new_code = response.choices[0].message.content
            elif model == "anthropic":
                response = await prompt_anthropic(code_generation_prompts[1], code_generation_prompt)
                new_code = response.contect

            # Code checking step
            code_checking_prompt = code_checking_prompts[1].replace("[[curr_code]]", new_code).replace("[[curr_step]]", planning_step)
            if model == "openai":
                response = await prompt_openai(code_checking_prompts[1], code_checking_prompt)
                code_check_result = response.choices[0].message.content
            elif model == "anthropic":
                response = await prompt_anthropic(code_checking_prompts[1], code_checking_prompt)
                code_check_result = response.contect

            if is_positive(code_check_result):
                break
            num_iterations += 1
        prev_code.append(new_code)
        prev_steps.append(planning_step)

    return "\n".join(prev_code)


async def code_refine_stage(model, problem, code, code_evaluation_prompts, code_regeneration_prompts, max_iterations=3):
    # Decide how to split code, for now doing it based on lines
    code_sections = code.split("\n")
    prev_sections = []
    for code_section in code_sections:
        num_iterations = 0
        curr_code = code_section
        while num_iterations < max_iterations:
            # Code evaluation section
            code_evaluation_prompt = code_evaluation_prompts[1].replace("[[curr_code]]", curr_code).replace("[[problem]]", problem).replace("[[prev_code]]", "\n".join(prev_sections))
            if model == "openai":
                response = await prompt_openai(code_evaluation_prompts[1], code_evaluation_prompt)
                code_evaluation_result = response.choices[0].message.content
            elif model == "anthropic":
                response = await prompt_anthropic(code_evaluation_prompts[1], code_evaluation_prompt)
                code_evaluation_result = response.contect

            if is_positive(code_evaluation_result):
                break

            code_regeneration_prompt = code_regeneration_prompts[1].replace("[[prev_code]]", "\n".join(prev_sections)).replace("[[problem]]", "\n".join(problem))
            if model == "openai":
                response = await prompt_openai(code_regeneration_prompts[1], code_regeneration_prompt)
                new_code = response.choices[0].message.content
            elif model == "anthropic":
                response = await prompt_anthropic(code_regeneration_prompts[1], code_regeneration_prompt)
                new_code = response.contect

            curr_code = new_code
        prev_sections.append(curr_code)

    return "\n".join(prev_sections)


async def self_refine(model, problem, planning_prompts, step_explaining_prompts, code_generation_prompts, code_checking_prompts, problem_prompt, max_iterations=3):
    plan = await planning_stage(model, planning_prompts, problem)
    planning_steps = parse_planning_response(plan)
    code = await refining_stage(model, planning_steps, step_explaining_prompts, code_generation_prompts, code_checking_prompts, problem_prompt, max_iterations)
    # Either save or evaluate code from here


async def ablation_self_refine(model, problem, planning_prompts, full_code_generation_prompts, code_evaluation_prompts, code_regeneration_prompts, max_iterations=3):
    plan = await planning_stage(model, planning_prompts, problem)
    initial_code = await full_code_generation(model, plan, problem, full_code_generation_prompts)
    code = await code_refine_stage(model, problem, initial_code, code_evaluation_prompts, code_regeneration_prompts, max_iterations)


if __name__ == "__main__":
    pass

