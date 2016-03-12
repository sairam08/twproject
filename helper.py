import re
from custom_exceptions import InvalidFormat, InvalidNumber


def custom_strip(string):
    """
    strips any preceding or trailing white spaces in a string
    :param string:
    :return: string
    """
    return string.strip()


def custom_int(string):
    """
    converts given integer in string format into integer and returns the value
    :param string:
    :return: integer
    """
    try:
        integer_value = int(string)
    except ValueError:
        raise InvalidNumber
    else:
        if integer_value < 0:
            raise InvalidNumber
        return integer_value


def process_input(input_message, expected_sample_pattern, function=custom_strip, split_char=None):
    """
    splits the values in input based on the split_char and applies function specified on each of the values
    :param input_message: (string) actual data to be processed
    :param expected_sample_pattern: (string) sample string depicting expected pattern
    :param function: (function pointer) function that is used to process the input obtained
    :param split_char: (character) character that is used to split the inputs
    :return:
    """
    values = map(function, input_message.split(split_char))
    if len(expected_sample_pattern.split(split_char)) != len(values) or None in values or '' in values:
        raise InvalidFormat(expected_sample_pattern)
    return values


def name_validator(input_string):
    pattern = re.compile('([A-Z]|[a-z]|[\.]|[\s])+')
    return True if pattern.match(input_string) else False