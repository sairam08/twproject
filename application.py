# -*- coding: utf-8 -*-

from game import Game
from constants import GlobalConstants
from custom_exceptions import TeamNotFound, InvalidFormat


def custom_strip(string):
    return string.strip()


def custom_int(string):
    integer_value = int(string)
    if integer_value < 0:
        raise ValueError
    return integer_value


def read_inputs_and_split_values(expected_sample_pattern, function=custom_strip, split_char=None):
    values = map(function, raw_input().split(split_char))
    if len(expected_sample_pattern.split(split_char)) != len(values):
        raise InvalidFormat(expected_sample_pattern)
    return values


def read_team_names():
    try:
        return read_inputs_and_split_values('India Brazil')
    except InvalidFormat as ex:
        print ex.message


def read_supporter():
    try:
        return read_inputs_and_split_values('Ravi, India', split_char=',')
    except InvalidFormat as ex:
        print ex.message


def read_reporter():
    try:
        return read_inputs_and_split_values('Vijay, CNN news', split_char=',')
    except InvalidFormat as ex:
        print ex.message


def read_supporter_and_reporter_count():
    try:
        return read_inputs_and_split_values('1 2', function=custom_int)
    except InvalidFormat as ex:
        print ex.message
    except ValueError as ex:
        print "A positive integer expected"


def get_team_name_from_message(message):
    return message.split(GlobalConstants.GOAL_KEYWORD)[1].strip()


def create_goal(game, team_name):
    try:
        team = game.goal(team_name)
        for person in game.supporters + game.reporters:
            person.print_goal_message(team)
    except TeamNotFound as ex:
        print ex.message


def complete(game):
    game.complete()
    for person in game.supporters + game.reporters:
        person.print_game_over_message(game)

if __name__ == '__main__':

    team_names = None

    while team_names is None:
        team_names = read_team_names()

    game = Game(team_names)

    counts = None
    while counts is None:
        counts = read_supporter_and_reporter_count()

    supporters_count = counts[0]
    reporters_count = counts[1]

    while len(game.supporters) < supporters_count:
        supporter_name, supporter_team = read_supporter()
        try:
            game.create_supporter(supporter_name, supporter_team)
        except TeamNotFound as ex:
            print ex.message

    while len(game.reporters) < reporters_count:
        reporter_name, reporter_channel = read_reporter()
        game.create_reporter(reporter_name, reporter_channel)

    while 1:
        input_message = raw_input()
        if GlobalConstants.GAME_OVER_KEYWORD in input_message:
            complete(game)
            exit(0)

        elif GlobalConstants.GOAL_KEYWORD in input_message:
            team_name = get_team_name_from_message(input_message)
            create_goal(game, team_name)
        else:
            print "invalid input should be either one of this {0} or {1}: <team_name>".\
                format(GlobalConstants.GAME_OVER_KEYWORD, GlobalConstants.GOAL_KEYWORD)
