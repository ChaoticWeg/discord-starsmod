from dhooks import Webhook, Embed
from datetime import datetime
from humanize import naturaltime

embed_color = 0xEE4433

reddit_icon = "http://www.redditstatic.com/new-icon.png"

footer_text = "Powered by PRAW"
footer_icon = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/110px-Python-logo-notext.svg.png"

def embed_from_listing(listing):
    """ Create a dhooks embed from a listing. Expects the listings to already be serialized. """

    listing_type = listing['type']
    listing_type = f"{listing_type[0].upper()}{listing_type[1:]}"
    title_text = f"{listing_type} reported in /r/DallasStars"

    # the resultant embed itself
    result = Embed(
        title=title_text,
        color=embed_color,
        url=listing['permalink'],
        timestamp=listing['timestamp']
    )

    # author
    result.set_author(
        name=f"/u/{listing['author']['name']}",
        url=f"https://reddit.com/u/{listing['author']['name']}",
        icon_url=listing['author']['icon_img']
    )

    # content field
    content_field = build_content_field(listing)
    result.add_field(**content_field)

    # mod reports field
    if len(listing['mod_reports']) > 0:
        result.add_field(**(build_reports_field(listing['mod_reports'], name="Mod Reports")))
    
    # user reports field
    if len(listing['user_reports']) > 0:
        result.add_field(**(build_reports_field(listing['user_reports'], name="User Reports")))
    
    # author field
    result.add_field(**(build_author_field(listing['author'], listing_type=listing_type)))

    # footer
    result.set_footer(
        text=footer_text,
        icon_url=footer_icon
    )

    # thumbnail - reddit icon
    result.set_thumbnail(reddit_icon)

    return result

def build_content_field(listing):
    field_name = listing['title'] if not listing['type'] == "comment" else listing['parent']['title']
    field_value = listing['content']
    return dict(name=field_name, value=field_value, inline=False)

def build_reports_field(reports, name=""):
    return dict(
        name=name,
        value='\n'.join([f"{report['user']} - {report['reason']}" for report in reports]),
        inline=False
    )

def build_author_field(author, listing_type="Item"):
    account_age = datetime.utcnow() - datetime.fromtimestamp(author['created_utc'])
    account_age_str = naturaltime(account_age)

    field_lines = [
        f"Account created {account_age_str}",
        f"Link karma: {author['link_karma']}",
        f"Comment karma: {author['comment_karma']}"
    ]

    return dict(
        name=f"{listing_type} posted by /u/{author['name']}",
        value='\n'.join(field_lines),
        inline=False
    )
