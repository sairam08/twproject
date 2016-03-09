from constants import GlobalConstants


class Person(object):

    MESSAGE = '{0} {1}: {2}'
    # 0 - name of the person
    # 1 - either 'says' or 'reports' or anything based on subclass verb parameter
    # 2 - actual message by the person

    def __init__(self, name):
        self.name = name
        self.verb = ''

    def print_message(self, message):
        print self.MESSAGE.format(self.name, self.verb, message)
