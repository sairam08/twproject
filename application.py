# -*- coding: utf-8 -*-

from game import Game
from team import Team
from constants import GlobalConstants


def custom_strip(string):
    return string.strip()


def read_team_names_and_create_teams(game):
    try:
        team_name1, team_name2 = map(custom_strip, raw_input().split())
        game.team1 = Team(team_name1)
        game.team2 = Team(team_name2)
        return [team_name1, team_name2]
    except:
        return 0


def read_supporter(game, team_names):
    try:
        supporter_name, supporter_team = map(custom_strip, raw_input().split(','))
        if supporter_team not in team_names:
            print "team name does not exist choose one among these ", ",".join(team_names)
            return 0
        game.create_supporters(supporter_name, supporter_team)
        return 1
    except:
        print "malformed input : sample valid input is as follows 'Ravi, India' , please input in correct format"
        return 0



def read_reporter(game):
    try:
        reporter_name, reporter_channel = map(custom_strip, raw_input().split(','))
        game.create_reporters(reporter_name, reporter_channel)
        return 1
    except:
        return 0


def read_supporter_and_reporter_count():
    try:
        supporter_count, reporter_count = map(int, raw_input().split(' '))
        return supporter_count, reporter_count
    except:
        return None, None


def create_goal(game, team_name, team_names):

    if isinstance(team_name, list):
        team_name = team_name[1]

    team_name = team_name.strip()

    if team_name in team_names:
        game.goal(team_name)
    else:
        print "team name does not exist choose one among these ", ",".join(team_names)


if __name__ == '__main__':

    current_game = Game()
    team_names = []
    supporter_count, reporter_count = 0, 0

    while 1:
        team_names = read_team_names_and_create_teams(current_game)
        if team_names:
            break
        print "malformed input : sample valid input is as follows 'India Brazil' , please input in correct format"

    while 1:
        supporter_count, reporter_count = read_supporter_and_reporter_count()
        if supporter_count:
            break
        print "malformed input : sample valid input is as follows '2 1' , please input in correct format"

    for i in range(supporter_count):
        if not read_supporter(current_game, team_names):
            read_supporter(current_game, team_names)

    for i in range(reporter_count):
        if not read_reporter(current_game):
            print "malformed input : sample valid input is as follows 'Vijay, CNN news', please input in correct format"
            read_reporter(current_game)

    while 1:
        input_message = raw_input()
        if GlobalConstants.GAME_OVER_KEYWORD in input_message:
            current_game.complete()
            exit(0)

        elif GlobalConstants.GOAL_KEYWORD in input_message:
            create_goal(current_game, input_message.split(GlobalConstants.GOAL_KEYWORD), team_names)
        else:
            print "invalid input should be either one of this {0} or {1} <team_name>".\
                format(GlobalConstants.GAME_OVER_KEYWORD, GlobalConstants.GOAL_KEYWORD)
