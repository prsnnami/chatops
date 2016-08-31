import re
from errbot import BotPlugin, re_botcmd

class FightBot(BotPlugin):
    """A cookiemonster bot"""

    @re_botcmd(pattern=r"(^| )single single( |$)", prefixed=False, flags=re.IGNORECASE)
    def single(self, msg, match):
        """Talk of cookies gives Errbot a craving..."""
        return "chill kta kti ho , chill"
