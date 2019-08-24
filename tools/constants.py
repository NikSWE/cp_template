from os import path

# paths
REPO_PATH = path.dirname(path.dirname(path.abspath(__file__)))
LOG_PATH = path.join(REPO_PATH, "tools/logs")

# programming lang
LANG_EXT = 'py'
LANG_COMMENT_SYMBOL = '#'

# commit emojis
EMOJI_AC = ':white_check_mark:'
EMOJI_WA = ':x:'
EMOJI_TLE = ':exclamation:'
EMOJI_INC = ':question:'

# commit messages
MSG_AC = 'accepted solution'
MSG_WA = 'wrong solution'
MSG_TLE = 'optimize solution'
MSG_INC = 'incomplete solution'