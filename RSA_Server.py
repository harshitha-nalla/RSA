import socket
import random
from sympy import randprime
from math import gcd

def generate_prime(a, b):
    p = randprime(a, b)
    q = randprime(a, b)
    while p == q:
        q = randprime(a, b)
    return p, q

def RSA_public_key(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    return e, n, phi

def RSA_private_key(e, phi):
    return pow(e, -1, phi)

def Decryption(cipher, d, n):
    return pow(cipher, d, n)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)

print("Server is waiting for a connection...")
conn, addr = server.accept()
print(f"Connected to {addr}")

p, q = generate_prime(100, 1000)
e, n, phi = RSA_public_key(p, q)
d = RSA_private_key(e, phi)

conn.send(f"{e},{n}".encode())

enc_msg = int(conn.recv(1024).decode())
dec_msg = Decryption(enc_msg, d, n)

if 32 <= dec_msg <= 126:
    dec_msg = chr(dec_msg)

print(f"Received Encrypted Message: {enc_msg}")
print(f"Decrypted Message: {dec_msg}")

conn.close()
server.close()
