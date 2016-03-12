from abc import ABCMeta, abstractmethod
from constants import GlobalConstants


class Person(object):
    __metaclass__ = ABCMeta

    MESSAGE = '{0} {1}: {2}'
    # 0 - name of the person
    # 1 - either 'says' or 'reports' or anything based on subclass verb parameter
    # 2 - actual message by the person

    def __init__(self, name):
        self.name = name
        self.verb = ''

    @abstractmethod
    def print_game_over_message(self, game):
        pass

    @abstractmethod
    def print_goal_message(self, team_secured_current_goal):
        pass

    def print_message(self, message):
        print self.MESSAGE.format(self.name, self.verb, message)

    def notify(self, notification_type, notification_data):
        if notification_type == GlobalConstants.GOAL_KEYWORD:
            self.notify_goal(notification_data)
        elif notification_type == GlobalConstants.GAME_OVER_KEYWORD:
            self.notify_game_over(notification_data)

    def notify_goal(self, team):
        self.print_goal_message(team)

    def notify_game_over(self, game):
        self.print_game_over_message(game)
