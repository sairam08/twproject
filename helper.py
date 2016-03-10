
from custom_exceptions import InvalidFormat


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