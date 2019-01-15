import json

def load(filepath):
    result = None
    try:
        with open(filepath, 'r') as infile:
            result = json.load(infile)
    except FileNotFoundError:
        pass
    return result

def dump(data, filepath):
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, sort_keys=False, indent=4)

def load_raw(filepath):
    result = None
    try:
        with open(filepath, 'r') as infile:
            result = infile.read()
    except FileNotFoundError:
        pass
    return result
