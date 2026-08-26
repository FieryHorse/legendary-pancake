N = int(input())

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [num for num in range(2, N + 1) if is_prime(num)]
print(*prime_numbers)


