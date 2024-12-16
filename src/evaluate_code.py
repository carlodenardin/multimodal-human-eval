import fire
import sys
import json
import ast
import os

import tqdm


from utils import stream_jsonl


GENERATED_CODE_FILE = './data/human eval/generated_code.jsonl'


def evaluate_code():

    for sample in tqdm.tqdm(stream_jsonl(GENERATED_CODE_FILE)):
        problem = sample["problem"]
        diagram_type = sample["diagram_type"]
        diagram_level = sample["diagram_level"]
        generated_code = sample["generated_code"]

        for folder in ['generated', 'official']:
            results, inputs, outputs = [], [], []

            test_path = f'data/human eval/test cases/{folder}/{problem}.jsonl'
            print(test_path)

            with open(test_path, 'r') as f:
                data = json.load(f)[0]
                inputs = ast.literal_eval(data['input']) if isinstance(
                    data['input'], str) else data['input']
                outputs = ast.literal_eval(data['output']) if isinstance(
                    data['output'], str) else data['output']

            assert len(inputs) == len(outputs)

            namespace = {}
            exec(generated_code, namespace)
            function = namespace[problem]

            for inp, out in zip(inputs, outputs):
                error = ""
                success = True
                try:
                    result = function(*inp) if isinstance(inp,
                                                          (tuple)) else function(inp)
                    if result != out:
                        success = False
                        error = f"Output different from Expected Output"

                except Exception as e:
                    error = f"Exception: {e}"
                    success = False

                results.append({
                    "success": success,
                    "error": error,
                    "input": inp,
                    "output": result,
                    "expected output": out,
                })

                path = f'data/human eval/results/{problem}/{diagram_type}/{diagram_level}/result_{folder}.jsonl'
                os.makedirs(os.path.dirname(path), exist_ok=True)

                with open(path, 'w', encoding='utf-8') as f:
                    for result in results:
                        json.dump(result, f)
                        f.write('\n')


def main():
    fire.Fire(evaluate_code)


sys.exit(main())
