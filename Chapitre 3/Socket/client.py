import socket

server_ip = "192.168.18.184"
server_port = 8099

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip,server_port))
request = raw_input("Hello les alphormeurlkjlkjs")
client.send(request)
response = client.recv(4096)
print response