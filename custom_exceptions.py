
class TeamNotFound(Exception):
    def __init__(self, given_team_name, available_teams):
        if given_team_name:
            message = "Given team - '{0}' does not exist, ".format(given_team_name)
        else:
            message = "Team name is not provided"
        self.message = "{0} please choose among these teams {1}".format(message, ",".join(available_teams))


class InvalidFormat(Exception):
    def __init__(self, expected_format):
        self.message = "malformed input : sample valid input is as follows '{0}' , please input in correct format".\
            format(expected_format)


class InvalidNumber(ValueError):
    def __init__(self):
        self.message = "Invalid input provided, expecting two positive integers"
