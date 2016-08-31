import logging

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Telegram'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_DATA_DIR = r'/home/prasanna/Projects/python/chatops/errbot-root/data'
BOT_EXTRA_PLUGIN_DIR = '/home/prasanna/Projects/python/chatops/errbot-root/plugins'

BOT_LOG_FILE = r'/home/prasanna/Projects/python/chatops/errbot-root/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_IDENTITY = {
    'token': '269871661:AAGjvgoGjfM80ARCtmMziUtTlzdOy5alTsA',
}

BOT_ADMINS = ('142595053', )  # !! Don't leave that to "CHANGE ME" if you connect your errbot to a chat system !!

CHATROOM_PRESENCE = ()
BOT_PREFIX = '/' 
