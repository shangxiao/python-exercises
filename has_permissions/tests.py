from . import Permission, has_permission


def test_has_permission__does_have_permission():
    assert has_permission(
        [
            Permission(name="can_view_documents", has_permission=True),
            Permission(name="can_edit_documents", has_permission=True),
            Permission(name="is_staff", has_permission=True),
        ]
    )


def test_has_permission__doesnt_have_permission():
    assert not has_permission(
        [
            Permission(name="can_view_documents", has_permission=True),
            Permission(name="can_edit_documents", has_permission=False),
            Permission(name="is_staff", has_permission=True),
        ]
    )
