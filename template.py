import os


from pathlib import Path
import logging

list_of_files=[
              
              "init_setup.sh",
              "requirements.txt",
              "requirements_dev.txt",
              "setup.py",
              "setup.cfg",
              "pyproject.toml",
              "tox.init",
              "experiment/experiments.ipynb" ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)  # Splits the path - Directory and filename
    if filedir:  # Check if filedir is not empty
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
