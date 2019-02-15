import paramiko
fo=open("iplist.txt")
for line in fo:
 ip=line.rstrip()
 #print(ip)
 ssh = paramiko.SSHClient()
 ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 ssh.connect(hostname=ip, username='root')
 stdin, stdout, stderr = ssh.exec_command('date')
 for line in stdout.read().splitlines():
    print(ip +" : " +line)

 ssh.close()

fo.close()

