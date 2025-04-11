from fibonacci import fibonacci

def test_fibonacci():
    """Test cases for the fibonacci function."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    assert fibonacci(15) == 610
    assert fibonacci(20) == 6765
    assert fibonacci(25) == 75025
    assert fibonacci(30) == 832040
    assert fibonacci(35) == 9227465
    assert fibonacci(40) == 102334155
    assert fibonacci(45) == 1134903170
    assert fibonacci(50) == 12586269025
