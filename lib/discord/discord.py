from os import path

webhook_url = None

def read_webhook_url(filename):
    global webhook_url
    with open(filename, 'r') as infile:
        webhook_url = infile.readline()

def test_webhook_url(errmsg="webhook URL not properly initialized"):
    global webhook_url
    assert webhook_url is not None, errmsg

def initialize():
    global webhook_url
    read_webhook_url(path.join(path.dirname(path.realpath(__file__)), 'webhook.dat'))
    test_webhook_url()
    print("read webhook url from file. url is %s" % webhook_url)

def alert_comment(comment):
    test_webhook_url()
    global webhook_url

    print('alerting report on comment with id %s' % comment.id)
