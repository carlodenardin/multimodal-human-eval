import requests
import base64

from openai import OpenAI
from const import Model, PROBLEMS

client = OpenAI()

# https://raw.githubusercontent.com/carlodenardin/multimodal-human-eval/refs/heads/main/data/diagrams/human%20eval/p84/fc/l1.drawio.png


def generate_code_openai(problem: str):

    prompt = f"Given a diagram that solves a problem, generate a runnable python function called {problem} that solve it. The code must follow some rules:\n- The function should get the inputs as parameters and return the output;\n- The function must be wrapped into ```python AND ```\n- Do not provide additional details or comment, just the code\n- Ensure that all indentations are correct.\n"

    """completion = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {
                "role": "user",
                "content": [
                        {"type": "text", "text": PROMPT},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": "https://raw.githubusercontent.com/carlodenardin/multimodal-human-eval/refs/heads/main/data/diagrams/human%20eval/p84/fc/l1.drawio.png",
                            }
                        },
                ],
            }
        ],
    )"""

    print(prompt)


def generate_code(model: Model):
    print(f"Generating code with {model.name}")

    if model.name == Model.OPENAI.name:
        for problem in PROBLEMS:
            generate_code_openai(problem)


def sum_digits_to_binary(n):
    return bin(sum(int(digit) for digit in str(n)))[2:]


if __name__ == '__main__':
    generate_code(model=Model.OPENAI)
    print(sum_digits_to_binary(3090))
