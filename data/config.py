from environs import Env
env = Env()
env.read_env()
BOT_TOKEN=env.str('BOT_TOKEN')
# ADMINS=env.list('ADMINS')
ADMINS = [5450565001, 1543122612]
CHANNELS = [-1002290216535]
KINO_CHANNEL = [-1002439890817]