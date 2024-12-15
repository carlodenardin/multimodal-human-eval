
GENERATED_CODE_FILE = './data/human_eval/diagrams/generated_code.jsonl'

for sample in tqdm.tqdm(stream_jsonl(generated_code_file)):
    function = sample["function"]
    generated_code = sample["generated_code"]
