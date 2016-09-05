from errbot import BotPlugin, botcmd, arg_botcmd, webhook, re_botcmd
import re
import string
import subprocess

commands = '''
cd ..
cd ..
cd django/src
'''

class Commands(BotPlugin):
    """
    bot commands
    """

    @botcmd(template="ls")
    def command(self,msg, args):
        if msg.frm.id == 142595053:
            output = subprocess.check_output( commands + args, shell=True).decode("utf-8")
            return {'data':output}

    @botcmd(template="ls")
    def git_clone(self, msg, args):
        output = subprocess.check_output(commands + "git clone " + args, shell=True).decode("utf-8")
        return {'data': output}

    @botcmd(template="ls")
    @arg_botcmd('first_name', type=str)
    @arg_botcmd('--last-name', dest='last_name', type=str)
    @arg_botcmd('--favorite', dest='favorite_number', type=int, default=42)
    def test(self, mess, first_name=None, last_name=None, favorite_number=None):
        return first_name, last_name

    @botcmd
    def git_revert(self, msg, args):
        x = []
        output = subprocess.check_output(commands + "git log --pretty=format:'%h %B'", shell=True).decode("utf-8")
        data = output.split("\n")
        msg.ctx['data'] = data
        return "enter the branch number (1/2/3/..) you want to revert \n" + output


    @botcmd
    def name(self, msg, args):
        return msg.ctx['data']

    @botcmd
    def git_pull(self, msg, args):
        output = subprocess.check_output(commands + "git pull", shell=True).decode("utf-8")
        return output

    @botcmd
    def branch(self, msg, args):
        num = (int(args) + 1) * 2
        branch = msg.ctx['data'][num]
        code = branch.split(" ")[0]
        msg.ctx['hash'] = code
        return "you selected branch " + args + ".  Enter /proceed to continue"


    @botcmd
    def proceed(self, msg, args):
        output = subprocess.check_output(commands + "git reset --hard " + msg.ctx['hash'], shell=True)
        return output
