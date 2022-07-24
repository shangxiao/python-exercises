from dataclasses import dataclass


@dataclass
class Permission:
    name: str
    has_permission: bool = False


def has_permission(permission_list):
    """
    Lessons:
      - all:  https://docs.python.org/3/library/functions.html#all
    """
    return all(permission.has_permission for permission in permission_list)
