import re

from . import generate_id


def test_valid_id():
    assert re.match("2[ABCDEFG012345]{3}-[ABCDEFG012345]{4}", generate_id())
