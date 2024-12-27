from itertools import product
from const import Model, PROMPT, HUMAN_EVAL_URL, BEGIN_TRIM, END_TRIM

from transformers import (
    PaliGemmaProcessor,
    PaliGemmaForConditionalGeneration,
)
from transformers.image_utils import load_image
import torch

from tqdm import tqdm
import json
import os

PROBLEMS = ['p84', 'p106', 'p108', 'p119', 'p120',
            'p126', 'p131', 'p147', 'p150', 'p155']
DIAGRAMS = ['fc', 'bpmn', 'block']
LEVELS = ['l1', 'l2', 'l3']


class CodeGenerator:
    """
    CodeGenerator class handles incremental code generation, 
    storing results in a JSONL file with each row composed by 4 keys:
    - problem: problem identifier (i.e. p84, ...)
    - diagram_type: type of diagram: Flowchart (fc), BPMN (bpmn), Block (block)
    - diagram_level: diagram level of detail from general to more specific: l1 -> l2 -> l3 
    - generated_code: code that has been generated from the model
    """

    def __init__(self, model: Model, output_path: str = "./data/human_eval"):
        """
        :param model: Your model or model identifier (i.e., Model.OPENAI).
        :param output_path: Folder where the JSONL file will be saved.
        """
        self.model = model
        self.output_file = os.path.join(
            output_path,
            f"{model.name.lower()}_generated_code.jsonl"
        )
        self.processed_items = self.load_processed_items(self.output_file)

        self.paligemma_id = "google/paligemma2-3b-pt-448"
        self.paligemma_model = PaliGemmaForConditionalGeneration.from_pretrained(
            self.paligemma_id,
            torch_dtype=torch.bfloat16,
            device_map="auto"
        ).eval()
        self.paligemma_processor = PaliGemmaProcessor.from_pretrained(
            self.paligemma_id)

    def generate_code(self):
        """
        Main entry point for generating code.
        Iterates over PROBLEMS, DIAGRAMS, LEVELS, and writes each generated record to JSONL.
        """
        print(f"Generating code with {self.model.name}")

        for problem in tqdm(PROBLEMS, desc="Processing problems"):
            for diagram in tqdm(DIAGRAMS, desc="Processing diagrams", disable=True):
                levs = LEVELS if diagram != "block" else ["l1"]
                for dl in tqdm(levs, desc="Processing diagram levels", disable=True):

                    key = (problem, diagram, dl)
                    if key in self.processed_items:
                        continue

                    image_url = f"{HUMAN_EVAL_URL}/{problem}/{diagram}/{dl}.drawio.png"

                    generated_code = ""

                    if self.model == Model.OPENAI:
                        generated_code = self.generate_code_openai(image_url)
                    elif self.model == Model.PALIGEMMA:
                        generated_code = self.generate_code_paligemma(
                            image_url)
                    else:
                        print("UNKNOWN MODEL")

                    record = {
                        "problem": problem,
                        "diagram_type": diagram,
                        "diagram_level": dl,
                        "generated_code": generated_code
                    }

                    self.write_record(self.output_file, record)
                    self.processed_items.add(key)

    def load_processed_items(self, filepath: str):
        processed = set()

        print(filepath)

        if not os.path.exists(filepath):
            with open(filepath, "w", encoding="utf-8"):
                pass
            return processed

        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                data = json.loads(line)
                key = (
                    data["problem"],
                    data["diagram_type"],
                    data["diagram_level"]
                )
                processed.add(key)

        return processed

    def trim_code(self, text: str):
        begin = text.find(BEGIN_TRIM) + len(BEGIN_TRIM)
        code = text[begin:]
        end = code.find(END_TRIM)

        if end != -1:
            code = code[:end]

        return code

    def write_record(self, filepath: str, record: dict):
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

    def generate_code_openai(self, image):
        """
        completion = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": PROMPT},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image,
                            }
                        },
                    ],
                    "temperature": 0.2,
                }
            ],
        )
        """
        return self.trim_code("completion.choices[0].message.content")

    def generate_code_paligemma(self, image_url: str) -> str:
        image = load_image(image_url)

        inputs = self.paligemma_processor(
            text=PROMPT,
            images=image,
            return_tensors="pt"
        ).to(torch.bfloat16).to(self.paligemma_model.device)

        input_len = inputs["input_ids"].shape[-1]

        with torch.inference_mode():
            generation = self.paligemma_model.generate(
                **inputs,
                max_new_tokens=1024,
                do_sample=False,
            )
            generation = generation[0][input_len:]
            decoded = self.paligemma_processor.decode(
                generation,
                skip_special_tokens=False,
            )

        print(decoded)

        return self.trim_code(decoded)


if __name__ == '__main__':

    print(PROMPT)
    openai_generator = CodeGenerator(
        Model.PALIGEMMA,
        output_path="./data/human_eval"
    )
    openai_generator.generate_code()
