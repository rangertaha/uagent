"""

"""
import random

import uastrings


class UserAgent:
    def __init__(self, category='all'):
        self.cat = category
        self.UAs = uastrings.UA
        self._methods()

    def all(self):
        if self.cat == 'all':
            a = []
            for k, v in self.UAs.items():
                a.extend(v)
            return a
        else:
            return self.UAs[self.cat]

    def count(self):
        return len(self.all())

    def random(self):
        return random.choice(self.all())

    def search(self, query, rand=True):
        results = []
        for ua in self.all():
            if query in ua:
                results.append(ua)
        if rand:
            return random.choice(results)
        return results

    def _methods(self):
        for k, v in self.UAs.items():
            setattr(self, k, v)
