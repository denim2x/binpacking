from binpacking.fixed_volume import fixed_volume, csv_to_constant_volume


def test_exact_fit():
    values = [1, 2, 1]
    bins = fixed_volume(values, 2)
    assert len(bins) == 2