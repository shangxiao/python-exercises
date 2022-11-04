import functools
import random

char = functools.partial(random.choice, "ABCDEFG012345")


def generate_id():
    return "2" + char() + char() + char() + "-" + char() + char() + char() + char()
