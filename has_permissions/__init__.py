from dataclasses import dataclass


@dataclass
class Permission:
    name: str
    has_permission: bool = False


def has_permission(permission_list):
    for permission in permission_list:
        if not permission.has_permission:
            return False

    return True
