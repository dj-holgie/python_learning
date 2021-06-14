import math
import time

prime_numbers = []
def is_prime_v1(n):    
    if n == 1:
        return False # 1 is not prime

    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    prime_numbers.append(n)
    return True

## Test Function
for n in range (1, 21):
    print(n, is_prime_v1(n))