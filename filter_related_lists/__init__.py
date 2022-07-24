WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
]


def filter_only_weekdays(labels, data):
    new_labels = []
    new_data = []

    for i in range(len(labels)):
        if labels[i] in WEEKDAYS:
            new_labels.append(labels[i])
            new_data.append(data[i])

    return (new_labels, new_data)
