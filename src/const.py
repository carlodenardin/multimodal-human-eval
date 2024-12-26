from enum import Enum


class Model(Enum):
    PALIGEMMA = 1
    LLAVA = 2
    OPENAI = 3


HUMAN_EVAL_URL = "https://raw.githubusercontent.com/carlodenardin/multimodal-human-eval/refs/heads/main/data/human%20eval/diagrams"


PROMPT = (
    f"Given a diagram that solves a problem, generate a runnable "
    f"python that solve it. The code must follow some rules:\n"
    f"- The function should get the inputs as parameters and "
    f"return the output;\n"
    f"- The function must be wrapped into ```python AND ```\n"
    f"- Do not provide additional details or comment, just the code\n"
    f"- Ensure that all indentations are correct.\n"
)
