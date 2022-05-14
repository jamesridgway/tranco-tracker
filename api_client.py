import os
from collections import OrderedDict
from datetime import datetime

import requests


class RankInfo:
    def __init__(self, data):
        self.ranks = OrderedDict()
        for rank in data['ranks']:
            date = datetime.strptime(rank['date'], "%Y-%m-%d")
            self.ranks[date] = rank['rank']

    def dates(self):
        return sorted(self.ranks.keys())

    def for_date(self, date):
        return self.ranks[date]


class TrancoApi:

    def __init__(self):
        self.username = os.getenv('TRANCO_USERNAME')
        self.password = os.getenv('TRANCO_API_KEY')
        print(self.username)
        print(self.password)

    def rank(self, domain):
        r = requests.get(f'https://tranco-list.eu/api/ranks/domain/{domain}', auth=(self.username, self.password))
        if r.status_code == 200:
            return RankInfo(r.json())
        return None
