# -*- coding: utf-8 -*-

from game import Game
from constants import GlobalConstants
from custom_exceptions import TeamNotFound, InvalidFormat, InvalidNumber
from helper import custom_int, process_input


class Application(object):
    """
    Reads, Parses all inputs and notifies the Game about the events and its respective details 
    """

    def __init__(self):
        self.game = None
        
    @staticmethod
    def read_game_input(): 
        # can be modified as needed in case input method changes at a later point
        return raw_input()

    @staticmethod
    def read_team_names():
        try:
            input_message = Application.read_game_input()
            return process_input(input_message, 'India Brazil')
        except InvalidFormat as ex:
            print ex.message

    @staticmethod
    def read_supporter():
        try:
            input_message = Application.read_game_input()
            return process_input(input_message, 'Ravi, India', split_char=',')
        except InvalidFormat as ex:
            print ex.message

    @staticmethod
    def read_reporter():
        """
        Reads input from console, parses the reporter details and returns the reporter name, reporter's channel 
        :return:  
        """
        try:
            input_message = Application.read_game_input()
            return process_input(input_message, 'Vijay, CNN news', split_char=',')
        except InvalidFormat as ex:
            print ex.message

    @staticmethod
    def read_supporter_and_reporter_count():
        try:
            input_message = Application.read_game_input()
            return process_input(input_message, '1 2', function=custom_int)
        except InvalidFormat as ex:
            print ex.message
        except InvalidNumber as ex:
            print ex.message

    @staticmethod
    def get_team_name_from_message(message):
        """
        Derives the team name by removing the Goal keyword from 'message'
        :param message: type(string)
        :return: type(string) team name
        """
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
        counts = None
        
        # loop iterates till the correct inputs are provided
        while team_names is None:
            team_names = self.read_team_names()

        self.game = Game(team_names)

        # loop iterates till all valid counts are provided
        while counts is None:
            counts = self.read_supporter_and_reporter_count()
        
        # input is expected to contain supporter count as first and reporter count as second 
        supporters_count = counts[0]
        reporters_count = counts[1]
        
        # loop iterates till all the supporters details are provided correctly
        while supporters_count:
            supporter_name, supporter_team = self.read_supporter()
            try:
                self.game.create_supporter(supporter_name, supporter_team)
                supporters_count -= 1
            except TeamNotFound as ex:
                print ex.message

        # loop iterates till all the reporters details are provided correctly
        while reporters_count:
            reporter_name, reporter_channel = self.read_reporter()
            reporters_count -= 1
            self.game.create_reporter(reporter_name, reporter_channel)

    def run(self):

        # loop iterates till game ends and will process only inputs that has either 'goal' or 'game over' related keys
        while 1:
            input_message = Application.read_game_input()
            
            # will trigger game complete and ends the application
            if GlobalConstants.GAME_OVER_KEYWORD in input_message:
                self.game.complete()
                exit(0)
            
            # if Goal input is passed its processed and notified to game
            elif GlobalConstants.GOAL_KEYWORD in input_message:
                team_name = Application.get_team_name_from_message(input_message)
                self.create_goal(team_name)
            else:
                print "invalid input_message should be either one of this {0} or {1}: <team_name>".\
                    format(GlobalConstants.GAME_OVER_KEYWORD, GlobalConstants.GOAL_KEYWORD)

#   entry point for the app
if __name__ == '__main__':

    # creating new app
    app = Application()
    
    # initializing the needed values
    app.initialize_game()
    
    # app starts processing goals till game is over
    app.run()
