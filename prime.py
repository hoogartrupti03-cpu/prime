def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))
n = 17
n = 

if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
