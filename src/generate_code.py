from itertools import product
from openai import OpenAI
from const import Model, HUMAN_EVAL_URL

from utils import trim_code, write_jsonl

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

    def __init__(self, model: Model, output_path: str = "./data/human eval"):
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

    def generate_code(self):
        """
        Main entry point for generating code.
        Iterates over PROBLEMS, DIAGRAMS, LEVELS, and writes each generated record to JSONL.
        """
        print(f"Generating code with {self.model}")

        for problem in tqdm(PROBLEMS, desc="Processing problems"):
            for diagram in tqdm(DIAGRAMS, desc="Processing diagrams", disable=True):
                levs = LEVELS if diagram != "block" else ["l1"]
                for dl in tqdm(levs, desc="Processing diagram levels", disable=True):

                    key = (problem, diagram, dl)
                    if key in self.processed_items:
                        continue

                    image_url = f"{HUMAN_EVAL_URL}/{problem}/{diagram}/{dl}.drawio.png"
                    """
                    generated_code = generate_code_openai(problem, image_url)

                    record = {
                        "problem": problem,
                        "diagram_type": diagram,
                        "diagram_level": dl,
                        "generated_code": generated_code
                    }

                    self.write_record(self.output_file, record)
                    self.processed_items.add(key)
                    """

    def load_processed_items(self, filepath: str):
        processed = set()

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

    def write_record(self, filepath: str, record: dict):
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

    def generate_code_paligemma():
        pass

    def generate_code_llava():
        pass

    def generate_code_openai():
        pass


if __name__ == '__main__':
    openai_generator = CodeGenerator(
        Model.OPENAI,
        output_path="./data/human eval"
    )
    openai_generator.generate_code()
