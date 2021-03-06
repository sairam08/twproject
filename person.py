from abc import ABCMeta, abstractmethod
from constants import GlobalConstants


class Person(object):
    # super class for match observers which contains the 'resultant Action on notification'
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
        # to be implemented by by the subclasses
        pass

    @abstractmethod
    def print_goal_message(self, team_secured_current_goal):
        # to be implemented by by the subclasses
        pass

    def print_message(self, message):
        # prints the final message of the observer
        print self.MESSAGE.format(self.name, self.verb, message)

    def notify(self, notification_type, notification_data):
        # triggers the Action related to the give notification type
        if notification_type == GlobalConstants.GOAL_KEYWORD:
            self.notify_goal(notification_data)
        elif notification_type == GlobalConstants.GAME_OVER_KEYWORD:
            self.notify_game_over(notification_data)

    def notify_goal(self, team):
        # calls the sub-class method
        self.print_goal_message(team)

    def notify_game_over(self, game):
        # calls the sub-class method
        self.print_game_over_message(game)
