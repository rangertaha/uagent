import random
import uastrings


class UserAgent:
    def __init__(self, category='all'):
        self.cat = category
        self.UAs = uastrings.UA

    def __repr__(self):
        return self.random(self.cat)

    def all(self):
        a = []
        for k, v in self.UAs.items():
            a.extend(v)
        return a

    def count(self, category='all'):
        if category == 'all':
            return len(self.all())
        if category in self.UAs.keys():
            return len(self.UAs[category])
        else:
            raise ValueError(
                "Options are: {0}".format(['all'] + self.UAs.keys()))

    def random(self, category='all'):
        if category == 'all':
            return random.choice(self.all())
        if category in self.UAs.keys():
            return self.UAs[category]
        else:
            raise ValueError(
                "Categories are: {0}".format(['all'] + self.UAs.keys()))


if __name__ == '__main__':
    u = UserAgent()
    # Counting the number of user agents in each category
    print '{0:15} {1:10}'.format('all', u.count('all'))
    for k, v in u.UAs.items():
        print '{0:15} {1:10}'.format(k, u.count(k))
    print '\nRandom User Agent:\n{0}\n'.format(u.random('all'))
    print 'UserAgent', UserAgent()
