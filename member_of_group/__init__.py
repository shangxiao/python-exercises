def is_member_of_group(name, *groups):
    """
    Lessons:
        1. in operator:  https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
                         https://docs.python.org/3/reference/expressions.html#in
    """
    is_member = False

    for group in groups:
        if name in group:
            is_member = True
            break

    return is_member
