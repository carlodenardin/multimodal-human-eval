import fire
import sys

from multimodal_human_eval.evaluation import evaluate_functional_correctness


def entry_point(
    samples_filename: str,
    problems_filename: str,
    k: str = "1,10",
    timeout: float = 3.0,
    n_workers: int = 4,
):
    print("Entry Point!")
    k = list(map(int, k.split(",")))

    evaluate_functional_correctness(
        samples_filename, problems_filename, k, timeout, n_workers
    )


def main():
    fire.Fire(entry_point)


sys.exit(main())
