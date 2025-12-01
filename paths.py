import sys
import os

ROOT = os.path.abspath(os.path.dirname(__file__))

paths = [
    os.path.abspath(os.path.join(ROOT, "controller")),
    os.path.abspath(os.path.join(ROOT, "view")),
    os.path.abspath(os.path.join(ROOT, "model")),
    os.path.abspath(os.path.join(ROOT, "model", "chain_of_responsability"))
    ]

for path in paths: 
    sys.path.append(path)