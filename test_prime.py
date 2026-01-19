from prime_number import is_prime
def test_is_prime_1():
    assert is_prime(5) == "prime"
def test_is_prime_2():
    assert is_prime(7) == "prime"
def test_is_prime_3():
    assert is_prime(10) == "not prime"

