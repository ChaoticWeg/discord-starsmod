import praw

class SerializableObject:
    """ An object that can be easily converted to a dict and JSON-serialized. """
    def serialize(self):
        return self.__dict__

class SerializableReport(SerializableObject):
    """ A user or mod report. """
    def __init__(self, report):
        self.reason = report[0]
        self.user = report[1]

class SerializableRedditor(SerializableObject):
    """ A redditor. """
    def __init__(self, redditor):
        self.name = redditor.name
        self.id = redditor.id
        self.icon_img = redditor.icon_img
        self.link_karma = redditor.link_karma
        self.comment_karma = redditor.comment_karma
        self.total_karma = self.link_karma + self.comment_karma
        self.created_utc = redditor.created_utc

class SerializableListing(SerializableObject):
    """ A listing that can be JSON-serialized. """
    def __init__(self, listing):
        self.permalink = f"https://reddit.com{listing.permalink}"
        self.author = SerializableRedditor(listing.author).serialize()
        self.mod_reports = [SerializableReport(r).serialize() for r in listing.mod_reports]
        self.user_reports = [SerializableReport(r).serialize() for r in listing.user_reports]
        self.num_reports = len(self.mod_reports) + len(self.user_reports)
        self.score = listing.score
        self.created_utc = listing.created_utc

        if is_comment(listing):
            self.type = "comment"
            self.content = listing.body
            self.parent = SerializableListing(get_submission_from_comment(listing)).serialize()
        elif is_submission(listing):
            self.type = "submission"
            self.content = listing.selftext if listing.selftext else "(empty)"
            self.title = listing.title
            self.parent = None
        else:
            self.type = "item"
            self.content = "(unknown)"
            self.title = "(unknown)"
            self.parent = None

def is_comment(listing):
    return isinstance(listing, praw.models.Comment)

def is_submission(listing):
    return isinstance(listing, praw.models.Submission)

def get_submission_from_comment(comment):
    """ Traverse the comment chain upwards until the root comment, then get the submission it belongs to """
    ancestor = comment
    refresh_counter = 0
    # get top-level comment of the chain this comment belongs to
    while not ancestor.is_root:
        ancestor = ancestor.parent()
        if refresh_counter % 9 == 0:
            ancestor.refresh()
        refresh_counter += 1
    # return the submission
    result = ancestor.parent()
    return result
