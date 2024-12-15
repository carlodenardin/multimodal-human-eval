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


def write_jsonl(filename: str, data: Iterable[Dict]):
    with open(filename, "wb") as fp:
        for x in data:
            fp.write((json.dumps(x) + "\n").encode("utf-8"))
