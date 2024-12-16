import os

import pkg_resources
from setuptools import setup

setup(
    name="src",
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    entry_points={
        "console_scripts": [
            "evaluate_code = src.evaluate_code:evaluate_code",
        ]
    },
)
