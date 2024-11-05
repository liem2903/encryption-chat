import random, math

def is_prime(number):
    if number < 2:
        return False 
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False 
    return True

def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value) 
    
    return prime

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d 
    raise(ValueError("Mod inverse does not exist"))

def find_prime_factors(N):
    array = []
    for i in range(2, int(math.sqrt(N)) + 1):
        print(f"Value is {i} and N is {N}")
        if N % i == 0:
            if is_prime(i) and is_prime(N // i):
                array.append((i, N // i))
                print(f"Successful pair: {i}, {N // i}")
    return array 