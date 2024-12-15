from typing import Iterable, Dict
import json

BEGIN_TRIM = "```python"
END_TRIM = "```"


def trim_code(text: str):
    begin = text.find(BEGIN_TRIM) + len(BEGIN_TRIM)
    code = text[begin:]
    end = code.find(END_TRIM)

    if end != -1:
        code = code[:end]

    return code


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
