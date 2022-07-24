def is_member_of_group(name, *groups):
    """
    Lessons:
        1. in operator:  https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
                         https://docs.python.org/3/reference/expressions.html#in
        2. any:  https://docs.python.org/3/library/functions.html#any
    """
    return any(name in group for group in groups)
