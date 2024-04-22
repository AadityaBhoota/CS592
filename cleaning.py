import json
import re

def create_mbpp_sanitized_examples():
    with open("./data/mbpp-sanitized-no-examples.jsonl", "r") as f:
        entries = list(f)

    # ['task_id', 'prompt', 'entry_point', 'canonical_solution', 'test']
    dataset = list(map(json.loads, entries))
    entry = dataset[0]

    with open("./data/mbpp.jsonl", "r") as f:
        entries = list(f)
    # ['text', 'code', 'task_id', 'test_setup_code', 'test_list', 'challenge_test_list']
    mbpp_dataset = list(map(json.loads, entries))

    for entry in dataset:
        task_id = int(entry["task_id"].replace("MbppEval/", ""))
        orig_mbpp = None
        for p in mbpp_dataset:
            if p["task_id"] == task_id:
                orig_mbpp = p
                break
        assert orig_mbpp != None
        # remove url links
        prompt = re.sub(r'https?:\/\/.*[\r\n]*', '', entry["prompt"])
        # add test case examples to prompt
        # temporarily remove end of comment
        prompt = prompt.removesuffix("    '''\n")
        prompt += "\n    Examples:\n"
        for tc in orig_mbpp["test_list"]:
            # ensure there's a space between ==
            tc = " == ".join(map(str.strip, tc.split("==")))
            tc = tc.replace("assert ", "    ")
            prompt += tc + "\n"
        # add end of comment
        prompt += "    '''\n"
        entry["prompt"] = prompt
        entry["text"] = orig_mbpp["text"]
        
    with open("./data/mbpp-sanitized-examples.json", "w") as f:
        json.dump(dataset, f, indent=4)
