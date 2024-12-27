import os
import requests
import torch

from const import *
from PIL import Image
from utils import *
from transformers import AutoProcessor, LlavaNextForConditionalGeneration, BitsAndBytesConfig
from tqdm import tqdm

MODELS = [
    "llava-hf/llava-v1.6-mistral-7b-hf",
    "llava-hf/llava-v1.6-vicuna-7b-hf",
]

MODELS_NAME = [
    "llava-mistral-7b",
    "llava-vicuna-7b",
]


class LlavaCodeGenerator:

    def __init__(self, model_id: str, file_name: str, problem_set: str):
        self.model_id = model_id
        self.file_name = file_name
        self.output_path = f"./data/{problem_set}"
        self.problem_set = problem_set
        self.problems = PROBLEMS_HUMAN_EVAL if problem_set == "human_eval" else PROBLEMS_PSB2
        """self.processor, self.model = self.setup()"""
        self.checkpoint = self.load_processed_items(
            f"{self.output_path}/{file_name}",
        )

    def generate(self):
        for problem in tqdm(self.problems, desc="Processing problems"):
            for diagram in tqdm(DIAGRAMS, desc="Processing diagrams", disable=True):
                levs = LEVELS if diagram != "block" else ["l1"]
                for dl in tqdm(levs, desc="Processing diagram levels", disable=True):

                    for run in range(MAX_RUN):

                        key = (problem, run, diagram, dl)
                        if key in self.checkpoint:
                            continue

                        image_url = f"https://raw.githubusercontent.com/carlodenardin/multimodal-human-eval/refs/heads/main/data/{self.problem_set}/diagrams/{problem}/{diagram}/{dl}.drawio.png"
                        generated_code = self.generate_code(image_url)

                        record = {
                            "problem": problem,
                            "run": run,
                            "diagram_type": diagram,
                            "diagram_level": dl,
                            "generated_code": generated_code
                        }

                        write_record(
                            f"{self.output_path}/{self.file_name}",
                            record,
                        )
                        self.checkpoint.add(key)

    def generate_code(self, image_url):
        image = Image.open(requests.get(image_url, stream=True).raw)

        conversation = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": PROMPT},
                    {"type": "image"},
                ],
            },
        ]

        prompt = processor.apply_chat_template(
            conversation, add_generation_prompt=True)

        inputs = processor(images=image, text=prompt,
                           return_tensors="pt").to("cuda")

        output = model.generate(**inputs, max_new_tokens=1024)

        return trim_code(processor.decode(output[0], skip_special_tokens=True))

    def load_processed_items(self, file_path: str):
        processed = set()

        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8"):
                pass
            return processed

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                data = json.loads(line)
                key = (
                    data["problem"],
                    data["run"],
                    data["diagram_type"],
                    data["diagram_level"]
                )
                processed.add(key)

        return processed

    def setup(self):
        processor = AutoProcessor.from_pretrained(self.model_id)

        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
        )

        model = LlavaNextForConditionalGeneration.from_pretrained(
            self.model_id,
            quantization_config=bnb_config,
            device_map={"": 0}
        )
        model.to("cuda")

        return processor, model


if __name__ == '__main__':

    for i in range(len(MODELS)):
        generate = LlavaCodeGenerator(
            MODELS[i],
            file_name=f"{MODELS_NAME[i]}.jsonl",
            problem_set="human_eval",
        )
        generate.generate()

    for i in range(len(MODELS)):
        generate = LlavaCodeGenerator(
            MODELS[i],
            file_name=f"{MODELS_NAME[i]}.jsonl",
            problem_set="psb2"
        )
        generate.generate()
