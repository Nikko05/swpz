import json
import os

def load_teams():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(dir_path, 'swpz/project/docs/plusliga/teamdata.json')
    
    with open(data_path, 'r', encoding='utf-8') as file:
        return json.load(file)
