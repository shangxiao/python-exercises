WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
]


def filter_only_weekdays(labels, data):
    """
    Lessons:
      1. enumerate() builtin:   https://docs.python.org/3/library/functions.html#enumerate

    """
    new_labels = []
    new_data = []

    for (i, label) in enumerate(labels):
        if label in WEEKDAYS:
            new_labels.append(label)
            new_data.append(data[i])

    return (new_labels, new_data)
