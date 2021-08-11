import socket

target_host = "google.com"
target_port = 80

# set up some data
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

# send some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive some data
response = client.recv(4096)

print(response.decode())
client.close()
