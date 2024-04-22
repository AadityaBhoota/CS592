from typing import List
from dataset import load_dataset
from execution import execute_code

def evaluate_human_eval(k=100):
    dataset = load_dataset("./data/HumanEval.jsonl")
    correct = 0
    total = len(dataset)
    for idx, entry in enumerate(dataset):
        # TODO either create prompt or pass in data directly
        prompt = entry["prompt"]
        # sample k solutions
        # TODO prompt framework in a batched way (async prompt n solutions)
        print("Running thru", idx / total)
        solutions = []
        print(f"Executing sols {idx / total}")
        for sol in solutions:
            # test_script = prompt + sol + "\n" + 
            test_script = entry["prompt"] + sol + "\n" + entry["test"] + f"\ncheck({entry['entry_point']})\n"
            passed = execute_code(test_script)
            if passed:
                break
        print(f"Evaluated {idx/ total}, Passed: {passed}")
        if passed:
            correct += 1
    percentage = correct / len(dataset) * 100
    print(f"Final: pass@{k}: {percentage}")
    

# def evaluate_mbpp():
#     dataset = load_dataset("./data/mbpp.jsonl")
#     prompts = []
#     for entry in dataset:
#         p = entry["text"]
#         if not entry["text"].endswith("."):
#             p += "."
        
#         p += " Your code should satisfy these tests: \n\n"
#         p += "\n".join(entry["test_list"]) + "\n"
#         prompts.append(p)
#     # TODO run framework
#     code_solutions: List[str] = []
#     passed = 0
#     for sol in code_solutions:
#         if execute_code(sol):
#             passed += 1
    