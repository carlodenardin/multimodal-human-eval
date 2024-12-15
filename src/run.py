from transformers import AutoProcessor, PaliGemmaForConditionalGeneration, BitsAndBytesConfig
from PIL import Image

import tqdm

from utils.const import PROMPT_INSTRUCTION
from multimodal_human_eval.data import read_problems, write_jsonl

BEGIN_TRIM = "```python"
END_TRIM = "```"

model_id = "google/paligemma-3b-mix-224"

bnb_config = BitsAndBytesConfig(load_in_8bit=True)
model = PaliGemmaForConditionalGeneration.from_pretrained(
    model_id, quantization_config=bnb_config)
processor = AutoProcessor.from_pretrained(model_id)

raw_image = Image.open('data/images/p100.png')


def trim_code(text: str):
    begin = text.find(BEGIN_TRIM) + len(BEGIN_TRIM)
    code = text[begin:]
    end = code.find(END_TRIM)

    if end != -1:
        code = code[:end]

    return code


def generate_completion(prompt: str):
    final_prompt = PROMPT_INSTRUCTION + prompt
    print(final_prompt)
    inputs = processor(raw_image, PROMPT_INSTRUCTION +
                       prompt, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=200)

    print(processor.decode(output[0], skip_special_tokens=True)[
          inputs.input_ids.shape[1]:])
    return trim_code(decoded)


problems = read_problems(dataset="./data/problems.jsonl")
n_samples = 1

samples = [
    dict(id=id, completion=generate_completion(problem["prompt"]))
    for id, problem in tqdm.tqdm(problems.items())
    for _ in tqdm.tqdm(range(n_samples), leave=False)
]

write_jsonl("./data/samples.jsonl", samples)
