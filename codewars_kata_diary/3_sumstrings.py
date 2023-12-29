# https://www.codewars.com/kata/5324945e2ece5e1f32000370/solutions/python

from codewars_kata_diary import testing

import itertools


def sum_strings(x: str, y: str) -> str:
    res, carry = [], 0

    for char_x, char_y in itertools.zip_longest(
        x[::-1], y[::-1], fillvalue="0"
    ):
        sum = int(char_x) + int(char_y) + carry
        res = [str(sum % 10)] + res  # preprending too slow
        carry = sum // 10

    return (str(carry) + "".join(res)).lstrip("0") or "0"


def sum_strings2(x: str, y: str) -> str:
    res, carry = [], 0

    for char_x, char_y in itertools.zip_longest(
        x[::-1], y[::-1], fillvalue="0"
    ):
        sum = int(char_x) + int(char_y) + carry
        res.append(str(sum % 10))  # appending faster than prepending
        carry = sum // 10

    return (str(carry) + "".join(res[::-1])).lstrip("0") or "0"


if __name__ == "__main__":
    inputs = [
        ("123", "456"),
        ("8797", "45"),
        ("800", "9567"),
        ("99", "1"),
        ("00103", "08567"),
        ("712569312664357328695151392", "8100824045303269669937"),
        ("50095301248058391139327916261", "81055900096023504197206408605"),
    ]
    expecteds = [
        "579",
        "8842",
        "10367",
        "100",
        "8670",
        "712577413488402631964821329",
        "131151201344081895336534324866",
    ]

    testing.test_func(inputs, expecteds, sum_strings)
