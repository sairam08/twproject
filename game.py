from constants import GlobalConstants
from supporter import Supporter
from reporter import Reporter


class Game(object):

    def __init__(self):
        self.team1 = None
        self.team2 = None
        self.supporters = []
        self.reporters = []

    def get_team_by_name(self, team_name):
        if self.team1 and self.team2:
            return self.team1 if team_name == self.team1.name else self.team2

    def create_supporters(self, supporter_name, supporting_team_name):
        supporting_team = self.get_team_by_name(supporting_team_name)
        supporter = Supporter(supporter_name, supporting_team)
        self.supporters.append(supporter)

    def create_reporters(self, reporter_name, news_channel):
        reporter = Reporter(reporter_name, news_channel)
        self.reporters.append(reporter)

    def goal(self, team_name):
        team = self.get_team_by_name(team_name)
        team.increase_goal_count()
        self.print_supporters_goal_message(team)
        self.print_reporters_goal_message(team)

    def complete(self):
        won_team, lost_team = self.get_won_and_lost_teams()
        self.print_supporters_game_over_message(won_team)
        self.print_reporters_game_over_message(won_team, lost_team)

    def get_won_and_lost_teams(self):
        if self.team1.goal_count == self.team2.goal_count:
            return None, None
        elif self.team1.goal_count > self.team2.goal_count:
            return self.team1, self.team2
        else:
            return self.team2, self.team1

    def print_supporters_goal_message(self, team):
        for supporter in self.supporters:
            supporter.print_goal_message(team)

    def print_supporters_game_over_message(self, won_team):
        for supporter in self.supporters:
            supporter.print_game_over_message(won_team)

    def print_reporters_goal_message(self, team):
        for reporter in self.reporters:
            reporter.print_goal_message(team)

    def print_reporters_game_over_message(self, won_team, lost_team):
        for reporter in self.reporters:
            reporter.print_game_over_message(won_team, lost_team)

