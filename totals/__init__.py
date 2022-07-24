def calculate_total_cost():
    """
    Lessons:
        1. Builtin sum():  https://docs.python.org/3/library/functions.html#sum
        2. List comprehension:  https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
    """
    return sum(
        [
            calculate_category_total(category)
            for category in ["rent", "utilities", "ingredients"]
        ]
    )


def calculate_category_total(category):
    # (for the purposes of this exercise assume this does some intricate calculation)
    return {
        "rent": 150,
        "utilities": 20,
        "ingredients": 100,
    }[category]
