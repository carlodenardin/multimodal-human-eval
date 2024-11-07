import ollama
import tqdm

from utils.const import PROMPT_INSTRUCTION
from multimodal_human_eval.data import read_problems, write_jsonl

BEGIN_TRIM = "```python"
END_TRIM = "```"


def trim_code(text: str):
    begin = text.find(BEGIN_TRIM) + len(BEGIN_TRIM)
    code = text[begin:]
    end = code.find(END_TRIM)

    if end != -1:
        code = code[:end]

    return code


def generate_completion(prompt: str):
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": PROMPT_INSTRUCTION + prompt,
            }
        ],
    )
    return trim_code(response["message"]["content"])


problems = read_problems(dataset="./data/problems.jsonl")

n_samples = 1

samples = [
    dict(id=id, completion=generate_completion(problem["prompt"]))
    for id, problem in tqdm.tqdm(problems.items())
    for _ in tqdm.tqdm(range(n_samples), leave=False)
]

write_jsonl("./data/samples.jsonl", samples)
