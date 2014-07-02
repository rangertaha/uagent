import unittest

import uagent


class TestUserAgentTestCase(unittest.TestCase):
    """
    Test methods on UserAgent(). Without specifying the category and defaulting
    to all categories.
    """
    def setUp(self):
        self.agent = uagent.UserAgent()

    def test_random(self):
        random_ua = self.agent.random()
        self.assertRaises(TypeError, random_ua, '')

    def test_count(self):
        count = self.agent.count()
        self.assertTrue(isinstance(count, int))

    def test_filter(self):
        filtered = self.agent.search('Linux')
        self.assertTrue(isinstance(filtered, str))
        self.assertTrue(filtered in self.agent.all())
        self.assertTrue('Linux' in filtered)

    def test_filter_list(self):
            filtered = self.agent.search('Linux', rand=False)
            self.assertTrue(isinstance(filtered, list))
            for item in filtered:
                self.assertTrue('Linux' in item)

    def test_browsers_attr(self):
        self.assertTrue(isinstance(self.agent.browsers, list))
        for ua in self.agent.browsers:
            self.assertTrue(ua in self.agent.UAs['browsers'])

    def test_crawlers_attr(self):
        self.assertTrue(isinstance(self.agent.crawlers, list))
        for ua in self.agent.crawlers:
            self.assertTrue(ua in self.agent.UAs['crawlers'])

    def test_link_checkers_attr(self):
        self.assertTrue(isinstance(self.agent.link_checkers, list))
        for ua in self.agent.link_checkers:
            self.assertTrue(ua in self.agent.UAs['link_checkers'])

    def test_validators_attr(self):
        self.assertTrue(isinstance(self.agent.validators, list))
        for ua in self.agent.validators:
            self.assertTrue(ua in self.agent.UAs['validators'])

    def test_feed_readers_attr(self):
        self.assertTrue(isinstance(self.agent.feed_readers, list))
        for ua in self.agent.feed_readers:
            self.assertTrue(ua in self.agent.UAs['feed_readers'])

    def test_email_clients_attr(self):
        self.assertTrue(isinstance(self.agent.email_clients, list))
        for ua in self.agent.email_clients:
            self.assertTrue(ua in self.agent.UAs['email_clients'])

    def test_mobile_attr(self):
        self.assertTrue(isinstance(self.agent.mobile, list))
        for ua in self.agent.mobile:
            self.assertTrue(ua in self.agent.UAs['mobile'])

    def test_libraries_attr(self):
        self.assertTrue(isinstance(self.agent.libraries, list))
        for ua in self.agent.libraries:
            self.assertTrue(ua in self.agent.UAs['libraries'])

    def test_offline_attr(self):
        self.assertTrue(isinstance(self.agent.offline, list))
        for ua in self.agent.offline:
            self.assertTrue(ua in self.agent.UAs['offline'])

    def test_others_attr(self):
        self.assertTrue(isinstance(self.agent.others, list))
        for ua in self.agent.others:
            self.assertTrue(ua in self.agent.UAs['others'])


if __name__ == '__main__':
    unittest.main()
