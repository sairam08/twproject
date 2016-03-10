from supporter import Supporter
from reporter import Reporter
from team import Team
from custom_exceptions import TeamNotFound


class Game(object):

    def __init__(self, team_names):
        self.team1 = Team(team_names[0])
        self.team2 = Team(team_names[1])
        self._winner = None
        self._loser = None
        self.supporters = []
        self.reporters = []

    @property
    def winner(self):
        return self._winner

    @property
    def loser(self):
        return self._loser

    def get_team_by_name(self, team_name):
        if self.team1 and self.team2:
            if team_name == self.team1.name:
                return self.team1
            elif team_name == self.team2.name:
                return self.team2
            else:
                raise TeamNotFound(team_name, [self.team1.name, self.team2.name])

    def create_supporter(self, supporter_name, supporting_team_name):
        supporting_team = self.get_team_by_name(supporting_team_name)
        supporter = Supporter(supporter_name, supporting_team)
        self.supporters.append(supporter)

    def create_reporter(self, reporter_name, news_channel):
        reporter = Reporter(reporter_name, news_channel)
        self.reporters.append(reporter)

    def get_subscribers(self):
        return self.supporters + self.reporters

    def notify_subscribers(self, notification_function, data_object):
        subscribers = self.get_subscribers()
        for subscriber in subscribers:
            function_name = getattr(subscriber, notification_function)
            function_name(data_object)

    def goal(self, team_name):
        team = self.get_team_by_name(team_name)
        team.increase_goal_count()
        self.notify_subscribers('notify_goal', team)

    def complete(self):
        self.set_winner_and_loser()
        self.notify_subscribers('notify_game_over', self)

    def is_match_tie(self):
        return self.team1.goal_count == self.team2.goal_count

    def set_winner_and_loser(self):
        if not self.is_match_tie():
            if self.team1.goal_count > self.team2.goal_count:
                self._winner, self._loser = self.team1, self.team2
            else:
                self._winner, self._loser = self.team2, self.team1



