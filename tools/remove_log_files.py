import constants as const
from shutil import rmtree

rmtree(const.LOG_PATH, ignore_errors=True)
print('Removed Logs')
