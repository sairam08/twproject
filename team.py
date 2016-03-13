class Team(object):

    def __init__(self, name):
        self.name = name
        self._goal_count = 0

    def increase_goal_count(self):
        self._goal_count += 1

    @property
    def goal_count(self):
        # property of team , acts as a getter and setter for _goal_count
        return self._goal_count
