import unittest

import uagent


class TestUserAgentFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)
        self.agent = uagent.UserAgent()

    def test_random_user_agent(self):
        agent = self.agent.random()
        agents = self.agent.all()
        self.assertRaises(TypeError, agent, agents)

    def test_random_category_uagent(self):
        agent = self.agent.random('all')
        self.assertTrue(agent in self.agent.all())

    def test_count_user_agents(self):
        all = self.agent.count('all')
        self.assertTrue(all == 10886)


if __name__ == '__main__':
    unittest.main()
