import day_06


# Test Part 1

def test_check_duplicates_return_false():
    sequence = "abcbd"
    result = day_06.check_duplicates(sequence)
    assert result == False

def test_check_duplicates_return_true():
    sequence = "abcd"
    result = day_06.check_duplicates(sequence)
    assert result == True