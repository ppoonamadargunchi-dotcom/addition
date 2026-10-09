from add import addition

def test_add():
    assert addition(2, 3) == 5

def test_add_zero():
    assert addition(5, 0) == 5

def test_add_negative():
    assert addition(-2, -3) == -5

def test_add_decimal():
    assert addition(2.5, 3.5) == 6.0