from errbot import BotPlugin, botcmd, arg_botcmd, webhook, re_botcmd
import re

class Fun(BotPlugin):
    """
    misc
    """
    @re_botcmd(pattern=r"(^| )cookies?( |$)", prefixed=False, flags=re.IGNORECASE)
    def listen_for_talk_of_cookies(self, msg, match):
        """Talk of cookies gives Errbot a craving..."""
        return "Cookies , yumm , mh ni khane :P"

    @re_botcmd(pattern=r"(^| )sale( |$)", prefixed=False, flags=re.IGNORECASE)
    def listen_for_sale(self, msg, match):
        """Talk of cookies gives Errbot a craving..."""
        return "tai sale"

    @re_botcmd(pattern=r"(^| )bhai( |$)", prefixed=False, flags=re.IGNORECASE)
    def listen_for_bhai(self, msg, match):
        """Talk of cookies gives Errbot a craving..."""
        return "hajur dai"

    @re_botcmd(pattern=r"(^| )single single( |$)", prefixed=False, flags=re.IGNORECASE)
    def single(self, msg, match):
        """Talk of cookies gives Errbot a craving..."""
        return "chill kta kti ho , chill"


    @botcmd(split_args_with=None)
    def example(self, message, args):
        """A command which simply returns 'Example'"""
        return "Example"

    @arg_botcmd('name', type=str)
    @arg_botcmd('--favorite-number', type=int, unpack_args=False)
    def say_hello(self, message, args):
        """
        A command which says hello to someone.

        If you include --favorite-number, it will also tell you their
        favorite number.
        """
        if args.favorite_number is None:
            return "Hello {name}".format(name=args.name)
        else:
            return "Hello {name}, I hear your favorite number is {number}".format(
                name=args.name,
                number=args.favorite_number,
            )
