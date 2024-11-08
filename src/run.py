from transformers import AutoProcessor, LlavaForConditionalGeneration
from transformers import BitsAndBytesConfig
from PIL import Image

# import ollama
import requests
import torch
import tqdm

from utils.const import PROMPT_INSTRUCTION
from multimodal_human_eval.data import read_problems, write_jsonl

BEGIN_TRIM = "```python"
END_TRIM = "```"

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)


model_id = "llava-hf/llava-1.5-7b-hf"

processor = AutoProcessor.from_pretrained(model_id)
model = LlavaForConditionalGeneration.from_pretrained(
    model_id, quantization_config=quantization_config, device_map="auto")

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
    inputs = processor(
        PROMPT_INSTRUCTION + prompts, images=image, padding=True, return_tensors="pt").to("cuda")

    # Generazione della risposta
    with torch.no_grad():
        generation = model.generate(
            **inputs, max_new_tokens=100, do_sample=False)

    # Decodifica il risultato
    decoded = processor.decode(generation[0], skip_special_tokens=True)
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
