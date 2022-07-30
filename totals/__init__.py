def calculate_total_cost():
    """
    Lessons:
        1. Augmented assignment:  https://docs.python.org/3/reference/simple_stmts.html#augmented-assignment-statements
    """
    total = 0
    categories = ["rent", "utilities", "ingredients"]
    for category in categories:
        total += calculate_category_total(category)

    return total


def calculate_category_total(category):
    # (for the purposes of this exercise assume this does some intricate calculation)
    return {
        "rent": 150,
        "utilities": 20,
        "ingredients": 100,
    }[category]
