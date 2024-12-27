PROBLEMS_HUMAN_EVAL = [
    'p84', 'p106', 'p108', 'p119', 'p120', 'p126', 'p131', 'p147', 'p150', 'p155',
]
PROBLEMS_PSB2 = [
    'find_pairs', 'leaders', 'spin_words', 'square_digits', 'vector_distance',
]
DIAGRAMS = ['fc', 'bpmn', 'block']
LEVELS = ['l1', 'l2', 'l3']

MAX_RUN = 1

PROMPT = (
    f"Understand the problem in the image and write a python "
    f"function called 'func' that solve it wrapped into ```python ```"
)
