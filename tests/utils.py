import json
import os


def load_json(fp):
    with open(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '../json_schemes')), fp)) as file:
        schema = json.load(file)
        return schema