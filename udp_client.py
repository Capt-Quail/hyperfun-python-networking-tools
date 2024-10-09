import socket

target_address = "0.0.0.1"
target_port = 9997

# Use of datagrgram socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# UDP = connectionless protocol, just send data
client.sendto(b"AAABBBCCC", (target_address, target_port))

data, addr = client.recvfrom(4096)

print(data.decode())
client.close()