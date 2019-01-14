from lib import reddit, paths, data

def scrape():
    reports = reddit.get_reports()
    print(f"got {len(reports)} reports from reddit: [{', '.join([report.id for report in reports])}]")
    return reports

def dump(reports):
    filepath = paths.relative(__file__, 'new_reports.json')
    serializable_reports = [reddit.SerializableListing(report) for report in reports]
    print(f"dumping {len(serializable_reports)} reports to {filepath}")
    serialized_reports = [report.serialize() for report in serializable_reports]
    data.dump(serialized_reports, filepath)

if __name__ == "__main__":
    reddit.initialize()
    reports = scrape()
    dump(reports)
