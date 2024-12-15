from enum import Enum


class Model(Enum):
    PALIGEMMA = 1
    LAVA = 2
    OPENAI = 3


PROBLEMS = ['p84', 'p106', 'p108', 'p119', 'p120',
            'p126', 'p131', 'p147', 'p150', 'p155']
DIAGRAMS = ['fc', 'bpmn', 'block']
DL = ['l1', 'l2', 'l3']
