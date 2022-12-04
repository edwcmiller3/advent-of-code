from day_03_part_01 import *


def test_priority():
    item = 'a'
    result = priority(item)
    assert result == 1


def test_shared_items():
    rucksacks = ('abc', 'cde')
    result = shared_items(rucksacks)
    assert result == 'c'


def test_split_rucksack():
    rucksack = 'abccde'
    result = split_rucksack(rucksack)
    assert result == ('abc', 'cde')


def test_string_middle():
    string = 'abccde'
    result = string_middle(string)
    assert result == 3