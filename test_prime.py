def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))
def test_is_prime():
    # Prime numbers
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(13) == True
    assert is_prime(17) == True
    
    # Non-prime numbers
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(9) == False
    assert is_prime(15) == False

    print("All tests passed!")

# Run tests
test_is_prime()
