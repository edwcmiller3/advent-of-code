import day_06


# Test Part 1

def test_unique_chunk_length():
    sequence = 'abcbd'
    result = day_06.unique_chunk_length(sequence)
    assert result == 4