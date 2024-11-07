from typing import Iterable, Dict

import json


def stream_jsonl(filename: str) -> Iterable[Dict]:
    with open(filename, "r") as fp:
        for line in fp:
            if any(not x.isspace() for x in line):
                yield json.loads(line)


def read_problems(dataset: str) -> Dict[str, Dict]:
    return {id["id"]: id for id in stream_jsonl(dataset)}


def write_jsonl(filename: str, data: Iterable[Dict]):
    with open(filename, "wb") as fp:
        for x in data:
            fp.write((json.dumps(x) + "\n").encode("utf-8"))
