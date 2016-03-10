class Team(object):

    def __init__(self, name):
        self.name = name
        self._goal_count = 0

    def increase_goal_count(self):
        self._goal_count += 1

    @property
    def goal_count(self):
        return self._goal_count
