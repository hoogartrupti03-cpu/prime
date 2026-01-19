def is_prime(n):
    # Check if the number is less than or equal to 1, which are not prime
    if n <= 1:
        return False
    # Check if n is 2 (the only even prime number)
    if n == 2:
        return True
    # Check if n is divisible by any number from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    n = int(input("Enter a number to check if it's prime: "))
    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
