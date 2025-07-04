import os
from pathlib import Path

list_of_files = [

    "app.py",
    "ingest.py",
    "requirements.txt",
    ".env",
    "pdfs/.gitkeep",
    "vector_store/.gitkeep",

    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/doubt_solver.py",
    "src/components/quiz_generator.py",
    "src/components/homework_checker.py",
    "src/components/roadmap_creator.py",

    "src/utils/__init__.py",
    "src/utils/embed_utils.py",
    "src/utils/translation_utils.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"✅ File already exists: {filepath}")
