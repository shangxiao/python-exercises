def calculate_total_cost():
    """
    Lessons:
        1. Augmented assignment:  https://docs.python.org/3/reference/simple_stmts.html#augmented-assignment-statements
        2. Builtin sum():  https://docs.python.org/3/library/functions.html#sum
    """
    totals = []
    for category in ["rent", "utilities", "ingredients"]:
        totals.append(calculate_category_total(category))

    return sum(totals)


def calculate_category_total(category):
    # (for the purposes of this exercise assume this does some intricate calculation)
    return {
        "rent": 150,
        "utilities": 20,
        "ingredients": 100,
    }[category]
