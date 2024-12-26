from enum import Enum


class Model(Enum):
    PALIGEMMA = 1
    LLAVA = 2
    OPENAI = 3


BEGIN_TRIM = "```python"
END_TRIM = "```"

HUMAN_EVAL_URL = "https://raw.githubusercontent.com/carlodenardin/multimodal-human-eval/refs/heads/main/data/human_eval/diagrams"


PROMPT = (
    f"Given a diagram that solves a problem, generate a runnable "
    f"python function called 'func' that solve it. The code must follow "
    f"some rules:\n"
    f"- The function should get the inputs as parameters and "
    f"return the output;\n"
    f"- The function must be wrapped into ```python AND ```\n"
    f"- Do not provide additional details or comment, just the code\n"
    f"- Ensure that all indentations are correct.\n"
)
