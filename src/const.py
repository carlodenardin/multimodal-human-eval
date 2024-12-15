from enum import Enum


class Model(Enum):
    PALIGEMMA = 1
    LLAVA = 2
    OPENAI = 3


HUMAN_EVAL_URL = "https://raw.githubusercontent.com/carlodenardin/multimodal-human-eval/refs/heads/main/data/human%20eval/diagrams"
PROBLEMS = ['p84', 'p106', 'p108', 'p119', 'p120',
            'p126', 'p131', 'p147', 'p150', 'p155']
DIAGRAMS = ['fc', 'bpmn', 'block']
DL = ['l1', 'l2', 'l3']
