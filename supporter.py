from person import Person


class Supporter(Person):

    SUPPORTER_TITLE_MESSAGE_VERB = 'says'

    SUPPORTER_EXPRESSION_ON_HIS_TEAM_GOAL = 'Hurrah!'
    SUPPORTER_EXPRESSION_ON_OPPOSITE_TEAM_GOAL = 'Alas!'

    SUPPORTER_EXPRESSION_ON_DRAW_MATCH = 'HMM! draw match'

    SUPPORTER_EXPRESSION_ON_HIS_TEAM_WIN = 'Yes! {0} won.'  # Yes! {India} won.
    SUPPORTER_EXPRESSION_ON_HIS_TEAM_LOSE = 'Alas! {0} lost.'  # Alas! {Brazil} lost.

    def __init__(self, name, team):
        super(Supporter, self).__init__(name)
        self.team = team
        self.verb = self.SUPPORTER_TITLE_MESSAGE_VERB

    def print_message(self, message):
        super(Supporter, self).print_message(message)

    def get_goal_message_based_on_team(self, team_secured_current_goal):
        return self.SUPPORTER_EXPRESSION_ON_HIS_TEAM_GOAL \
            if team_secured_current_goal == self.team else self.SUPPORTER_EXPRESSION_ON_OPPOSITE_TEAM_GOAL

    def print_goal_message(self, team_secured_current_goal):
        goal_message = self.get_goal_message_based_on_team(team_secured_current_goal)
        self.print_message(goal_message)

    def get_game_over_message_based_on_team(self, winning_team):
        message_format = self.SUPPORTER_EXPRESSION_ON_HIS_TEAM_WIN \
            if winning_team == self.team else self.SUPPORTER_EXPRESSION_ON_HIS_TEAM_LOSE
        return message_format.format(self.team.name)

    def print_game_over_message(self, game):
        if game.is_match_tie():
            game_over_message = self.SUPPORTER_EXPRESSION_ON_DRAW_MATCH
        else:
            game_over_message = self.get_game_over_message_based_on_team(game.winner)
        self.print_message(game_over_message)
