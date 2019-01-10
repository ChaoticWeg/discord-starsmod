from os import path
import praw, json

reddit = None

def read_creds(filename):
    file_data = None
    with open(filename, 'r') as infile:
        file_data = json.load(infile)
    return file_data

def initialize():
    global reddit
    creds = read_creds(path.join(path.dirname(path.realpath(__file__)), 'creds.json'))
    reddit = praw.Reddit(**creds)

    test_reddit()
    print("initialized PRAW reddit instance for %s" % reddit.user.me())

def test_reddit():
    global reddit
    assert reddit is not None, "PRAW reddit instance was not properly initialized"

def read_reports_since():
    global reddit
    test_reddit()
