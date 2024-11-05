from asymmetric_encryption import find_prime_factors, mod_inverse

n = int(input("What is the value of n: "))
publicKey = int(input("What is the value of the public key"))

# Finding all prime factors of n.
primeNumbers = find_prime_factors(n)
phiArray = []
# Finding all phi values: 
for p, q in primeNumbers:
    phiArray.append((p - 1) * (q - 1))
privateKeys = []
# Find all private keys by inversing it.
for phi in phiArray:
    privateKeys.append(mod_inverse(publicKey, phi))

print(privateKeys)