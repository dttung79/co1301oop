from demo_function import add, get_rank

def test_add_01():
    actual = add(1, 0)
    expected = 1
    assert actual == expected

def test_add_02():
    actual = add(0, 0)
    expected = 0
    assert actual == expected

def test_add_03():
    actual = add(1, 1)
    expected = 2
    assert actual == expected


## tests for get_rank
def test_get_rank_01():
    assert get_rank(30) == 'Fail'

def test_get_rank_02():
    assert get_rank(40) == 'Pass'

def test_get_rank_03():
    assert get_rank(50) == 'Pass'

def test_get_rank_04():
    assert get_rank(60) == 'Merit'

def test_get_rank_05():
    assert get_rank(70) == 'Merit'

def test_get_rank_06():
    assert get_rank(80) == 'Merit'

def test_get_rank_07():
    assert get_rank(90) == 'Distinction'

def test_get_rank_08():
    assert get_rank(100) == 'Distinction'

def test_get_rank_09():
    assert get_rank(0) == 'Fail'

def test_get_rank_10():
    assert get_rank(-100) == 'Invalid'

def test_get_rank_11():
    assert get_rank(1000) == 'Invalid'

def test_get_rank_12():
    assert get_rank(10000000000) == 'Invalid'

def test_get_rank_13():
    assert get_rank('hello') == 'Invalid'