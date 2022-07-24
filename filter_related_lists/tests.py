from . import filter_only_weekdays


def test_filter_labels_and_data():

    labels = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    data = [5, 2, 3, 1, 8, 6, 7]

    (new_labels, new_data) = filter_only_weekdays(labels, data)

    assert new_labels == [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
    ]
    assert new_data == [5, 2, 3, 1, 8]
