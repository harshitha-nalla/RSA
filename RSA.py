from sympy import randprime
from math import gcd
import random
import socket

def generate_prime(a,b):
    p=randprime(a,b)
    q=randprime(a,b)
    while p==q:
        q=randprime(a,b)
    return p,q

def RSA_public_key(p,q):
    n=p*q
    phi=(p-1)*(q-1)
    e=random.randint(1,phi)
    while gcd(e,phi)!=1:
        e=random.randint(1,phi)
    return e,n,phi

def RSA_private_key(e,phi):
    d=pow(e,-1,phi)
    return d

def Encryption(plain_msg,e,n):
    cipher=pow(plain_msg,e)%n
    return cipher

def Decryption(cipher,d,n):
    plain=pow(cipher,d)%n
    return plain

msg=input("Enter the message:")
flag=0
if msg.isdigit():
    msg=int(msg)
elif msg.isalpha():
    msg=ord(msg)
    flag=1
p,q=generate_prime(1,1000)
e,n,phi=RSA_public_key(p,q)
d=RSA_private_key(e,phi)
enc_msg=Encryption(msg,e,n)
dec_msg=Decryption(enc_msg,d,n)
if flag==1:
    dec_msg=chr(dec_msg)
print(f"The Encrypted message is: {enc_msg}")
print(f"The Decrypted message is: {dec_msg}")