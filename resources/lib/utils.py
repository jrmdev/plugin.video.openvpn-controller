import re
import xbmc
import xbmcaddon
import xbmcgui

from urllib import quote_plus
from urlparse import parse_qsl
from subprocess import check_output

def get_addon():
    return xbmcaddon.Addon()

def get_addon_id():
    """Helper function for returning the version of the running add-on"""
    return get_addon().getAddonInfo('id')

def get_addon_name():
    """Helper function for returning the version of the running add-on"""
    return get_addon().getAddonInfo('name')

def get_addon_version():
    """Helper function for returning the version of the running add-on"""
    return get_addon().getAddonInfo('version')

def log(s):
    xbmc.log("[%s v%s] %s" % (get_addon_name(), get_addon_version(), s.encode('utf-8')), level=xbmc.LOGNOTICE)

def handle_error(message):
    if isinstance(message, str):
        message = message.split('\n')

    message = ["%s v%s" % (get_addon_name(), get_addon_version())] + message

    xbmcgui.Dialog().ok(*message)

def uri_to_dict(s):
    return {k: v for k, v in parse_qsl(s.lstrip('?'))}

def escape_ansi(line):
    ret = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ret.sub('', line)

def command(cmd, silent=False):
    res = check_output(cmd)
    res = res.encode('utf-8', 'ignore')
    res = escape_ansi(res)
    res = res.strip()
    if not silent:
        handle_error(res)
    else:
        return res