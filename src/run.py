from transformers import AutoProcessor, PaliGemmaForConditionalGeneration
from PIL import Image

# import ollama
import requests
import torch
import tqdm

from utils.const import PROMPT_INSTRUCTION
from multimodal_human_eval.data import read_problems, write_jsonl

BEGIN_TRIM = "```python"
END_TRIM = "```"

model_id = "google/paligemma-3b-mix-224"

model = PaliGemmaForConditionalGeneration.from_pretrained(model_id).eval()
processor = AutoProcessor.from_pretrained(model_id)

url = "https://www.w3resource.com/w3r_images/python-programming-puzzles-image-exercise-4-a.png"
image = Image.open(requests.get(url, stream=True).raw)


def trim_code(text: str):
    begin = text.find(BEGIN_TRIM) + len(BEGIN_TRIM)
    code = text[begin:]
    end = code.find(END_TRIM)

    if end != -1:
        code = code[:end]

    return code


def generate_completion(prompt: str):
    final_prompt = PROMPT_INSTRUCTION + prompt
    model_inputs = processor(
        text=final_prompt, images=image, return_tensors="pt")
    input_len = model_inputs["input_ids"].shape[-1]

    with torch.inference_mode():
        generation = model.generate(
            **model_inputs, max_new_tokens=100, do_sample=False)
        generation = generation[0][input_len:]
        decoded = processor.decode(generation, skip_special_tokens=True)
        print(decoded)
    return trim_code(decoded)


problems = read_problems(dataset="./data/problems.jsonl")

n_samples = 1

samples = [
    dict(id=id, completion=generate_completion(problem["prompt"]))
    for id, problem in tqdm.tqdm(problems.items())
    for _ in tqdm.tqdm(range(n_samples), leave=False)
]

write_jsonl("./data/samples.jsonl", samples)
