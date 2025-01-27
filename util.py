from datetime import datetime
from time import strftime

import pytz


def register(function_list):
    for f in function_list:
        f()

# FIXME
def format_date(date):
    return strftime('**(%A)** %Y. %m. %d. %H:%M',
                    datetime.fromtimestamp(date.microsecond / 1000, tz=pytz.timezone('Etc/GMT+1')).timetuple())
