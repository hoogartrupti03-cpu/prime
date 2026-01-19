def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
is_prime = is_prime_number(number)

print(f"{number} is {'a prime' if is_prime else 'not a prime'}")
