"""Test name-matching regular expression."""
from ast import pattern
import re

import pytest


# *** ADD YOUR PATTERN BELOW *** #
pattern = r"^[A-Z]+(([',. -])?[a-zA-Z]*)+ [A-Z]+(([',. -])?[a-zA-Z]*)*$"
# *** ADD YOUR PATTERN ABOVE *** #

# Describe in what situations your solution will fail.
"""This solution will fail if the name has a number in it, or if the name has a special character in it."""
test_cases = [
    ("Quan Hongchan", True),
    ("Philip Seymour Hoffman", True),
    ("Dr. Nicki Washington", True),
    ("Joseph Gordon-Levitt", True),
    ("Ken Griffey, Jr.", True),
    ("John von Neumann", True),
    ("Cher", False),
    ("not a name", False),
    ("happy feet", False),
    ("The end", False),
]


@pytest.mark.parametrize("string,matches", test_cases)
def test_name_matching(string, matches: bool):
    """Test whether pattern correctly matches or does not match input."""
    assert (re.fullmatch(pattern, string) is not None) == matches
