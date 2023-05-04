import ../my_module

def test_multiply():
    assert my_module.multiply(2, 3) == 6
    assert my_module.multiply(5, 0) == 0
    assert my_module.multiply(-1, 1) == -1
    assert my_module.multiply(-1, -1) == 1
