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
      2. List comprehensions:  https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions

    """
    new_data = [item for (i, item) in enumerate(data) if labels[i] in WEEKDAYS]
    new_labels = [label for label in labels if label in WEEKDAYS]

    return (new_labels, new_data)
