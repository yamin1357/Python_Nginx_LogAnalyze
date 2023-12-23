from datetime import datetime

from termcolor import colored

old_print = print


def timestamped_print(*args, **kwargs):
    old_print(colored(f"{datetime.now()}", 'cyan'), *args, **kwargs)


print = timestamped_print
