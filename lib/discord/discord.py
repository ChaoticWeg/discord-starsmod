from dhooks import Webhook
from .embeds import embed_from_listing
from lib import paths, data

_hook_url_filename = '.webhook_debug'
_hook_instance = None

def read_url(filename):
    return data.load_raw(paths.relative(__file__, filename))

def create_hook():
    global _hook_instance
    _hook_instance = Webhook(read_url(_hook_url_filename))
    return _hook_instance

def get_hook():
    global _hook_instance
    return _hook_instance if _hook_instance is not None else create_hook()

def announce_report(report):
    get_hook().send(username="StarsMod", embed=embed_from_listing(report))
