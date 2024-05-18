import os


from pathlib import Path
import logging

list_of_files=[
              "github_workflows/.gitkeep",
              "src/init__.py",
              "src/components/__init__.py"
              "src/components/data_ingestion.py",
              "src/components/data_transformation.py",
              "src/components/model_trainer.py",
              "src/components/model_evaluation.py",
              "src/pipeline/__init__.py",
              "src/pipeline/training_pipeline.py",
              "src/pipeline/prediction_pipeline.py",
              "src/utils/__init__.py",
              "src/utils/utils.py",
              "src/logger/logging.py",
              "src/exception/exception.py",
              "test/unit/__init__.py",
              "test/integration/__init__.py",
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
    if filepath != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for file: {filename}")  # Corrected logger code
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass

