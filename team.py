class Team(object):

    def __init__(self, name):
        self.name = name
        self.goal_count = 0

    def increase_goal_count(self):
        self.goal_count += 1
