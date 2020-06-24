from binpacking.fixed_count import fixed_count


def test_only_zero_weights():
    values = [0, 0, 0]
    bins = fixed_count(values, 4)
    assert bins == [[0, 0, 0], [], [], []]
