import praw, json

from lib import paths, data

reddit = None

def __read_creds():
    return data.load(paths.relative(__file__, 'creds.json'))

def __read_known_reports():
    return data.load(paths.relative(__file__, 'known_reports.json'))

def __write_known_reports(reports):
    data.dump(reports, paths.relative(__file__, 'known_reports.json'))

def __test_reddit(errmsg="PRAW reddit instance was not properly initialized"):
    global reddit
    assert reddit is not None, errmsg

def initialize():
    global reddit

    # read creds and use them to initialize reddit
    creds = __read_creds()
    reddit = praw.Reddit(**creds)

    __test_reddit()
    print("initialized PRAW reddit instance for %s" % reddit.user.me())

def get_reports():
    global reddit

    # get reports from reddit
    reports_data = reddit.subreddit('dallasstars').mod.reports()
    known_reports = __read_known_reports()
    known_reports = [] if known_reports is None else known_reports

    # filter out known reports
    unknown_reports = [report for report in reports_data if not report.id in known_reports]

    # now we know about them :)
    known_reports.extend([report.id for report in unknown_reports])
    __write_known_reports(known_reports)

    return unknown_reports
