# -*- coding: utf-8 -*-

from game import Game
from constants import GlobalConstants
from custom_exceptions import TeamNotFound, InvalidFormat
from helper import custom_int, read_inputs_and_split_values


class Application(object):

    def __init__(self):
        self.game = None

    @staticmethod
    def read_team_names():
        try:
            return read_inputs_and_split_values('India Brazil')
        except InvalidFormat as ex:
            print ex.message

    @staticmethod
    def read_supporter():
        try:
            return read_inputs_and_split_values('Ravi, India', split_char=',')
        except InvalidFormat as ex:
            print ex.message

    @staticmethod
    def read_reporter():
        try:
            return read_inputs_and_split_values('Vijay, CNN news', split_char=',')
        except InvalidFormat as ex:
            print ex.message

    @staticmethod
    def read_supporter_and_reporter_count():
        try:
            return read_inputs_and_split_values('1 2', function=custom_int)
        except InvalidFormat as ex:
            print ex.message
        except ValueError as ex:
            print "A positive integer expected"

    @staticmethod
    def get_team_name_from_message(message):
        return message.split(GlobalConstants.GOAL_KEYWORD)[1].strip()

    def create_goal(self, team_name):
        try:
            self.game.goal(team_name)
        except TeamNotFound as ex:
            print ex.message

    def complete(self):
        self.game.complete()

    def initialize_game(self):

        team_names = None
        while team_names is None:
            team_names = self.read_team_names()

        self.game = Game(team_names)

        counts = None
        while counts is None:
            counts = self.read_supporter_and_reporter_count()

        supporters_count = counts[0]
        reporters_count = counts[1]

        while supporters_count:
            supporter_name, supporter_team = self.read_supporter()
            try:
                self.game.create_supporter(supporter_name, supporter_team)
                supporters_count -= 1
            except TeamNotFound as ex:
                print ex.message

        while reporters_count:
            reporter_name, reporter_channel = self.read_reporter()
            reporters_count -= 1
            self.game.create_reporter(reporter_name, reporter_channel)

    def run(self):

        while 1:
            input_message = raw_input()
            if GlobalConstants.GAME_OVER_KEYWORD in input_message:
                self.game.complete()
                exit(0)

            elif GlobalConstants.GOAL_KEYWORD in input_message:
                team_name = Application.get_team_name_from_message(input_message)
                self.create_goal(team_name)
            else:
                print "invalid input should be either one of this {0} or {1}: <team_name>".\
                    format(GlobalConstants.GAME_OVER_KEYWORD, GlobalConstants.GOAL_KEYWORD)

if __name__ == '__main__':

    app = Application()

    app.initialize_game()
    app.run()
