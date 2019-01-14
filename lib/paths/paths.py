from os import path

def relative(src, target):
    return path.join(path.dirname(path.realpath(src)), target)
