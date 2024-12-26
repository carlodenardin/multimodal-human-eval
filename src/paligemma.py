from transformers import (
    PaliGemmaProcessor,
    PaliGemmaForConditionalGeneration,
)
from transformers.image_utils import load_image
import torch

model_id = "google/paligemma2-3b-pt-448"

url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
image = load_image(url)

model = PaliGemmaForConditionalGeneration.from_pretrained(
    model_id, torch_dtype=torch.bfloat16, device_map="auto").eval()
processor = PaliGemmaProcessor.from_pretrained(model_id)

# Leaving the prompt blank for pre-trained models
prompt = ""
model_inputs = processor(text=prompt, images=image, return_tensors="pt").to(
    torch.bfloat16).to(model.device)
input_len = model_inputs["input_ids"].shape[-1]

with torch.inference_mode():
    generation = model.generate(
        **model_inputs, max_new_tokens=100, do_sample=False)
    generation = generation[0][input_len:]
    decoded = processor.decode(generation, skip_special_tokens=True)
    print(decoded)


"""
def generate_code_openai(problem: str, url: str):

    completion = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {
                "role": "user",
                "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": url,
                            }
                        },
                ],
                "temperature": 0.2,
            }
        ],
    )

    return trim_code(completion.choices[0].message.content)


def generate_code(model: Model):
    print(f"Generating code with {model.name}")

    if model.name == Model.OPENAI.name:

        samples = [
            dict(
                problem=problem,
                diagram_type=diagram,
                diagram_level=dl,
                generated_code=generate_code_openai(
                    problem, f"{HUMAN_EVAL_URL}/{problem}/{diagram}/{dl}.drawio.png"),
            )
            for problem in tqdm(PROBLEMS, desc='Processing problems', disable=True)
            for diagram in tqdm(DIAGRAMS, desc='Processing diagrams')
            for dl in tqdm((DL if diagram != 'block' else ['l1']), desc='Processing diagram levels', disable=True)
        ]

        write_jsonl(
            "./data/human eval/generated_code.jsonl", samples)

    elif model.name == Model.PALIGEMMA.name:
        pass
    elif model.name == Model.LLAVA.name:
        pass"""
