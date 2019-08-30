# utils.py
import json
import os

def write_file(file_path, data):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file)

def load_file(file_path):
    with open(file_path, "r") as json_file:
        return json.load(json_file)

def check_file(file_path):
        if os.path.isfile(file_path + ".json") == False:
                write_file(file_path, "{}")