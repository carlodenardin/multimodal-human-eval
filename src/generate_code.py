from itertools import product
from openai import OpenAI
from const import Model, HUMAN_EVAL_URL, PROBLEMS, DIAGRAMS, DL

from utils import trim_code, write_jsonl

from tqdm import tqdm

client = OpenAI()


def generate_code_openai(problem: str, url: str):

    prompt = f"Given a diagram that solves a problem, generate a runnable python function called {problem} that solve it. The code must follow some rules:\n- The function should get the inputs as parameters and return the output;\n- The function must be wrapped into ```python AND ```\n- Do not provide additional details or comment, just the code\n- Ensure that all indentations are correct.\n"

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
                "temperature": 0.7,
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
        pass


if __name__ == '__main__':
    generate_code(model=Model.OPENAI)
