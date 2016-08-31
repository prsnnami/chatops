from errbot import BotPlugin, botcmd
import subprocess

class HelloWorld(BotPlugin):
    """Example 'Hello, world!' plugin for Errbot"""

    @botcmd
    def hello(self, msg, args):
        """Say hello to the world"""
        return "Hello, world!"

    @botcmd(template="ls")
    def ls(self,msg, args):
        output = subprocess.check_output("ls").decode("utf-8")
        data = output.split("/n")
        return {'data' : output}
