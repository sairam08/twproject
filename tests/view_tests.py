from helper import process_input, custom_int, custom_strip
from unittest import TestCase
from test_constants import ApplicationInputParsingTestData


class TestApplicationInputParsing(TestCase):

    def setUp(self):
        self.correct_pattern = ''
        self.split_char = None
        self.function_to_apply = None
        self.positive_test_cases = []
        self.exception_test_cases = []

    def set_data(self, correct_pattern,  positive_test_cases, exception_tet_cases, split_char=None,
                 function=custom_strip):
        self.correct_pattern = correct_pattern
        self.split_char = split_char
        self.function_to_apply = function
        self.positive_test_cases = positive_test_cases
        self.exception_test_cases = exception_tet_cases

    def test_input_types(self):
        for input_type in ApplicationInputParsingTestData:
            self.set_data(input_type["correct_pattern"], input_type["positive_test_cases"],
                          input_type["exception_test_cases"], input_type["split_char"], input_type["function"])
            self.run_for_input_type()

    def run_for_input_type(self):
        for test_case in self.positive_test_cases:
            result = process_input(test_case[0], self.correct_pattern, function=self.function_to_apply,
                                   split_char=self.split_char)
            assert result == test_case[1]

        for test_case in self.exception_test_cases:
            self.assertRaises(test_case[1], process_input, test_case[0], self.correct_pattern,
                              function=self.function_to_apply, split_char=None)


