from helper import custom_int, custom_strip
from custom_exceptions import InvalidFormat, InvalidNumber

ApplicationInputParsingTestData = [
    {
        "correct_pattern": "India Brazil",
        "split_char": None,
        "function": custom_strip,
        "positive_test_cases": [
            ('India     Brazil', ['India', 'Brazil']),
            ('India Brazil', ['India', 'Brazil'])
        ],
        "exception_test_cases": [
            ('India', InvalidFormat),
            ('India ', InvalidFormat),
            ('India      ', InvalidFormat),
            ('', InvalidFormat),
            ('   ', InvalidFormat)
        ]

    },
    {
        "correct_pattern": "1 2",
        "split_char": None,
        "function": custom_int,
        "positive_test_cases": [
            ('1          2', [1, 2]),
            ('1 2', [1, 2])
        ],
        "exception_test_cases": [
            ('-1', InvalidNumber),
            ('-1 -2', InvalidNumber),
            ('1 -2', InvalidNumber),
            ('1', InvalidFormat),
            ('1 ', InvalidFormat),
            ('1      ', InvalidFormat),
            ('', InvalidFormat),
            ('   ', InvalidFormat)
        ]
    },
    {
        "correct_pattern": "Rahul, Brazil",
        "split_char": ',',
        "function": custom_strip,
        "positive_test_cases": [
            ('Rahul  ,  Brazil', ['Rahul', 'Brazil']),
            ('Rahul,  Brazil', ['Rahul', 'Brazil']),
            ('Rahul  ,Brazil', ['Rahul', 'Brazil'])
        ],
        "exception_test_cases": [
            ('Rahul', InvalidFormat),
            ('Rahul ', InvalidFormat),
            ('Rahul      ', InvalidFormat),
            ('', InvalidFormat),
            ('   ', InvalidFormat)
        ]

    }


]