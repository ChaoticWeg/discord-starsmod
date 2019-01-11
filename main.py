from lib import reddit, discord

def run():
    for comment in reddit.read_reports_since():
        discord.alert_comment(comment)

if __name__ == "__main__":
    reddit.initialize()
    discord.initialize()

    run()
