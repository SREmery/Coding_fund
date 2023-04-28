def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1
    return sum

def test_count_int():
    assert count([1, 2, 3, 4, 2, 4, 2], 2) == 3
    assert count([1, 2, 3, 4, 2], 4) == 1
    assert count([], 2) == 0
    assert count([1, 2, 3], 4) == 0 

def test_count_str():
    assert count(["apple", "apple", "pear", "orange"], "apple") == 2
    assert count([], "banana") == 0
    assert count(["apple", "apple", "pear"], "orange") == 0 