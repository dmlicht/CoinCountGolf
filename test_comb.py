from comb_golf import count_combinations
def test_pytest():
    print 'okay'
    assert True

def test_count_combinations():
    expected = 10
    result = count_combinations([5, 10], 100)
    assert expected == result
