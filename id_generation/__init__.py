import random


def generate_id():
    the_id = "".join([random.choice("ABCDEFG012345") for _ in range(7)])
    the_id = f"2{the_id}"
    the_id = "-".join((the_id[:4], the_id[4:]))
    return the_id
