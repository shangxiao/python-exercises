from . import is_member_of_group

police_academy = {
    "cadets": [
        "Carey Mahoney",
        "Moses Hightower",
        "Leslie Barbara",
        "Larvell Jones",
        "George Martin",
        "Eugene Tackleberry",
        "Douglas Fackler",
        "Laverne Hooks",
        "Kyle Blankes",
        "Chad Copeland",
    ],
    "trainers": [
        "Lieutenant Harris",
        "Sargeant Callahan",
    ],
    "seniority": [
        "Commandant Lassard",
        "Chief Hurst",
    ],
}


def test_is_member_of_group__is_member():
    assert is_member_of_group(
        "Carey Mahoney",
        police_academy["cadets"],
        police_academy["trainers"],
        police_academy["seniority"],
    )


def test_is_member_of_group__isnt_member():
    assert not is_member_of_group(
        "Carey Mahoney",
        police_academy["trainers"],
        police_academy["seniority"],
    )
