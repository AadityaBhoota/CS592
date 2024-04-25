import json
import os
import re
from typing import Dict, List

# TODO this is very messay and jank


def load_humaneval_dataset(filepath: str) -> List[Dict]:
    """
    Returns list of dicts, where each dict contains:
    - task_id
    - prompt: python code with docstring describing problem, like code completion problem
    - entry_point: name of main function
    - canonical_solution: code for solution (has no function signature)
    - test: function string containing a bunch of asserts in a function with signature "def check(candidate)", where candidate is function to use
    """
    with open(filepath, "r") as f:
        json_lines = list(f)
    dataset = list(map(json.loads, json_lines))
    return dataset


def load_mbpp_dataset(filepath: str) -> List[Dict]:
    """
    Returns list of dicts, where each dict contains
    - task_id
    - text: textual description of problem
    - code: solution (has function signature)
    - test_setup_code: code imports for running tests
    - test_list: list of assert stmts
    - challenge_test_list: list of assert stmts
    """
    with open(filepath, "r") as f:
        json_lines = list(f)
    dataset = list(map(json.loads, json_lines))
    return dataset


def load_mbpp_sanitized_dataset(filepath: str) -> List[Dict]:
    """
    Returns list of dicts, where each dict contains
    - source_file
    - task_id
    - prompt: textual description of problem
    - code: solution (has function signature)
    - test_imports: list of import stmts
    - test_list: list of assert stmts
    """
    with open(filepath, "r") as f:
        dataset = json.load(f)
    # some preprocesssing/cleaning
    for entry in dataset:
        # removes urls
        entry["prompt"] = re.sub(r'https?:\/\/.*[\r\n]*', '', entry["prompt"]).strip()
    return dataset

