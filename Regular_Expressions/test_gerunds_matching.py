"""Test gerunds-matching regular expression.
if input is a text, split each line into words and check if each word is a gerund."""
from ast import pattern
import re

import pytest

"""filter gerunds using verb + ing, verb usually contain [aeiou]"""
"""filter out something/nothing/etc"""
pattern = r".*[aeiou]+[^th]*ing$"

test_cases = [
    ("running", True),
    ("coming", True),
    ("living", True),
    ("cunning", True),
    ("showering", True),
    ("walking", True),
    ("sing", False),
    ("king", False),
    ("nothing", False),
    ("ring", False),
]


@pytest.mark.parametrize("string,matches", test_cases)
def test_gerunds_matching(string, matches: bool):
    """Test whether pattern correctly matches or does not match input."""
    assert (re.fullmatch(pattern, string) is not None) == matches
