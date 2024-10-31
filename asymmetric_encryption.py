import random 

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