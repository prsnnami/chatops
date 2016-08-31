import re
from errbot import BotPlugin, re_botcmd

class CookieBot(BotPlugin):
    """A cookiemonster bot"""

    @re_botcmd(pattern=r"(^| )cookies?( |$)", prefixed=False, flags=re.IGNORECASE)
    def listen_for_talk_of_cookies(self, msg, match):
        """Talk of cookies gives Errbot a craving..."""
        return "Cookies , yumm , mh ni khane :P"

    @re_botcmd(pattern=r"(^| )sale( |$)", prefixed=False, flags=re.IGNORECASE)
    def listen_for_sale(self, msg, match):
        """Talk of cookies gives Errbot a craving..."""
        return "tai sale"
