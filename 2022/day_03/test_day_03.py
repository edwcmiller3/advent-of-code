import day_03_part_01
import day_03_part_02

# Part 1 Tests

def test_priority():
    item = 'a'
    result = day_03_part_01.priority(item)
    assert result == 1


def test_shared_items():
    rucksacks = ('abc', 'cde')
    result = day_03_part_01.shared_items(rucksacks)
    assert result == 'c'


def test_split_rucksack():
    rucksack = 'abccde'
    result = day_03_part_01.split_rucksack(rucksack)
    assert result == ('abc', 'cde')


def test_string_middle():
    string = 'abccde'
    result = day_03_part_01.string_middle(string)
    assert result == 3

# Part 2 Tests

def test_common_among_group():
    group = ('abc', 'cde', 'cfg')
    result = day_03_part_02.common_among_group(group)
    assert result == 'c'
