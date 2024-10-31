import json
import socket, random, math
from asymmetric_encryption import is_prime, generate_prime, mod_inverse

p, q = generate_prime(10, 50), generate_prime(10, 50)

while p == q:
    q = generate_prime(10, 50)
# Calculating Eulers Totient Function.
n = p * q 
phi_n = (p-1) * (q-1)
# Calculating public key - is larger than 2 and a co-prime and smaller than phi n.
e = random.randint(3, phi_n - 1)
while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n - 1)
# Calculating private key.
d = mod_inverse(e, phi_n) 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 13550))

done = False 
# Sending out private key.
client.send((str(e)).encode('utf-8'))
# Receiving server public key.
publicKey = int(client.recv(1024).decode('utf-8'))
# Send out n
client.send((str(n)).encode('utf-8'))
primeNumber = int(client.recv(1024).decode('utf-8'))

while not done: 
    encodeMsg = [ord(c) for c in (input("Message: "))]
    cipherText = [pow(c, publicKey, primeNumber) for c in encodeMsg]
    serialized_array = json.dumps(cipherText).encode('utf-8')
    client.sendall(serialized_array)

    bytes_array = json.loads(client.recv(1024).decode('utf-8'))
    encode_msg = [pow(c, d, n) for c in bytes_array]
    msg = "".join(chr(ch) for ch in encode_msg)

    if msg == 'quit':
        done = True
    else: 
        print(msg)

client.close()
