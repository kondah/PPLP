import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bind_ip = "0.0.0.0"
bind_port = 8099

server.bind((bind_ip, bind_port))
server.listen(2)
print "[+] Listening on address %s and port %d" %(bind_ip,bind_port)

(client, (ip, port)) = server.accept()

print "Client IP address is : %s " %ip
print "Client remote port is : %s " %port

data = 'noob'
response = 'Thanks for contacting me'

while len(data):

    data = client.recv(2048)
    print "Client sent : ",data
    client.send(response)

print "Closing the connections "
client.close()
print "Shutting down the server"
server.close()



