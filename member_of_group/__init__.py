def is_member_of_group(name, *groups):
    is_member = False

    for group in groups:
        for member in group:
            if name == member:
                is_member = True
                break

    return is_member
