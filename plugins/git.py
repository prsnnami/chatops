from errbot import botflow, FlowRoot, BotFlow
from subprocess import check_output
import commands

commands = '''
cd ..
cd ..
cd django/src
'''

class Git(BotFlow):
    """ Conversation flows for Errbot"""

    @botflow
    def git(self, flow: FlowRoot):
        """ Docs for the flow example comes here """
        first_step = flow.connect('git_revert', auto_trigger=True)           # first is a command name from any loaded plugin.
        second_step = first_step.connect('branch')
        third_step = second_step.connect('proceed')
