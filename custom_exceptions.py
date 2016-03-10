
class TeamNotFound(Exception):
    def __init__(self, given_team_name, available_teams):
        self.message = "Given team - '{0}' does not exist, please choose among these teams {1}".\
            format(given_team_name, ",".join(available_teams))


class InvalidFormat(Exception):
    def __init__(self, expected_format):
        self.message = "malformed input : sample valid input is as follows '{0}' , please input in correct format".\
            format(expected_format)
