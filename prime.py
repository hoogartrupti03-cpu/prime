def is_prime_numbers():
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))
    
if __name__ == "__main__":
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
