from person import Person
import time


class Reporter(Person):

    REPORTER_TITLE_MESSAGE_VERB = 'reports'

    REPORTER_MESSAGE = '{0} Brought to you by {1}.'
    # {India has won the game against Brazil by 1-0.} Brought to you by {CNN news}.

    REPORTER_MESSAGE_ON_GOAL = '{0} has scored a goal at {1}.'
    # {India} has scored a goal at {9:30am}.

    REPORTER_MESSAGE_ON_GAME_OVER = '{0} has won the game against {1} by {2}-{3}.'
    # {India} has won the game against {Brazil} by {1}-{0}.

    REPORTER_MESSAGE_ON_GAME_DRAW = 'The match concluded as a tie.'

    def __init__(self, name, news_channel_name):
        super(Reporter, self).__init__(name)
        self.news_channel = news_channel_name
        self.verb = self.REPORTER_TITLE_MESSAGE_VERB

    def print_message(self, message):
        message = self.REPORTER_MESSAGE.format(message, self.news_channel)
        super(Reporter, self).print_message(message)

    @staticmethod
    def get_goal_message(team_secured_current_goal):
        return Reporter.REPORTER_MESSAGE_ON_GOAL.format(team_secured_current_goal.name,
                                                        time.strftime('%I:%M %p').lower())

    def print_goal_message(self, team_secured_current_goal):
        """
        prints the message on a team making a goal
        :param team_secured_current_goal: Team to which current goal corresponds to
        :return: None
        """
        goal_message = Reporter.get_goal_message(team_secured_current_goal)
        self.print_message(goal_message)

    @staticmethod
    def get_game_over_message(won_team, lost_team):
        return Reporter.REPORTER_MESSAGE_ON_GAME_OVER.format(won_team.name, lost_team.name,
                                                             won_team.goal_count, lost_team.goal_count)

    def print_game_over_message(self, game):
        """
        prints the Game complete message
        :param game: Game object
        :return:None
        """
        if game.is_match_tie():
            game_over_message = self.REPORTER_MESSAGE_ON_GAME_DRAW
        else:
            game_over_message = Reporter.get_game_over_message(game.winner, game.loser)
        self.print_message(game_over_message)
