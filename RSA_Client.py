
import socket

def Encryption(plain_msg, e, n):
    return pow(plain_msg, e, n)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

e, n = map(int, client.recv(1024).decode().split(","))
print(f"Received Public Key: (e={e}, n={n})")

msg = input("Enter a number or a letter: ")

if msg.isdigit():
    msg = int(msg)
else:
    msg = ord(msg)

enc_msg = Encryption(msg, e, n)

client.send(str(enc_msg).encode())
print(f"Encrypted Message Sent: {enc_msg}")

client.close()
