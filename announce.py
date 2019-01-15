from lib import discord, data, paths

def announce_all():
    """ Load new reports from new_reports.json and announce each report to the Discord webhook """
    reports = data.load(paths.relative(__file__, 'new_reports.json'))
    for report in reports:
        discord.announce_report(report)

if __name__ == "__main__":
    announce_all()
