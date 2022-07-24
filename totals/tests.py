from . import calculate_total_cost


def test_totals():
    assert calculate_total_cost() == 270
