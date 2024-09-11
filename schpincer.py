import pytz
import requests
import json
from datetime import datetime
from time import strftime


def fetch(url):
    return requests.get(url).text


def parse(j):
    json_array = json.loads(j)
    openings = []
    for j in json_array:
        try:
            o = Opening(
                {"circleName": j["circleName"],
                 "nextOpeningDate": j["nextOpeningDate"]
                 }
            )
            if o not in openings and j["orderable"]:
                openings.append(o)
        except Exception:
            pass
    return openings

class Opening(object):
    def __init__(self, j):
        self.__dict__ = j
        self.__dict__.update(
            {'nextOpeningDate': strftime('**(%A)** %Y. %m. %d. %H:%M', datetime.fromtimestamp(
                self.__dict__.get("nextOpeningDate") / 1000, tz=pytz.timezone('Etc/GMT-1')).timetuple())
             }
        )

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__.get("circleName") == other.__dict__.get("circleName")
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return str(self.__dict__.get("circleName")) + " " + str(self.__dict__.get("nextOpeningDate")) + " " + str(
            self.__dict__.get("orderable"))
