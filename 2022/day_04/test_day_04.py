import day_04


# Test Part 1

def test_parse_ranges():
    section_range = "10-15"
    splitter = '-'
    result = day_04.parse_range(section_range, splitter)
    assert type(result) == tuple
    assert result == ('10', '15')


def test_generate_ranges():
    parsed_range = ('10', '15')
    result = day_04.generate_range_set(parsed_range)
    assert type(result) == set
    assert result == {10, 11, 12, 13, 14, 15}


def test_find_subsets_return_0():
    range_set_A, range_set_B = {1, 2}, {3, 4}
    result = day_04.find_subsets(range_set_A, range_set_B)
    assert result == 0


def test_find_subsets_return_1():
    range_set_A, range_set_B = {1, 2, 3}, {1, 2}
    result = day_04.find_subsets(range_set_A, range_set_B)
    assert result == 1


# Test Part 2

def test_find_overlap_return_0():
    range_set_A, range_set_B = {1, 2}, {3, 4}
    result = day_04.find_overlap(range_set_A, range_set_B)
    assert result == 0


def test_find_overlap_return_1():
    range_set_A, range_set_B = {1, 2, 3}, {2, 4}
    result = day_04.find_overlap(range_set_A, range_set_B)
    assert result == 1