def is_member_of_group(name, *groups):
    """
    Lessons:
        1. in operator:  https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
                         https://docs.python.org/3/reference/expressions.html#in
    """
    for group in groups:
        if name in group:
            return True

    return False
