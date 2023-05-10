import paramiko
import time



hostname = '158.160.26.139'
myuser = 'timur'
mySSHK = 'C:/Users/timur/.ssh/id_ed25519.pub' ## поменять на вход по паролю
sshcon = paramiko.SSHClient()  # will create the object
sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # no known_hosts error
sshcon.connect(hostname, username=myuser, key_filename=mySSHK)  # no passwd needed

stdin, stdout, strerr = sshcon.exec_command('sudo apt update')
stdin, stdout, strerr = sshcon.exec_command('sudo apt install apt-transport-https ca-certificates curl software-properties-common')
stdin, stdout, stderr = sshcon.exec_command("acidiag touch clean; y | reload")
time.sleep(10)
stdin, stdout, strerr = sshcon.exec_command('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
time.sleep(10)
stdin, stdout, strerr = sshcon.exec_command('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"')

stdin, stdout, stderr = sshcon.exec_command("acidiag touch clean; '[ENTER]' | reload")
time.sleep(10)
stdin, stdout, strerr = sshcon.exec_command('sudo apt update')
# for line in iter(lambda: stdout.readline(2048), ""):
#     print(line)
stdin, stdout, strerr = sshcon.exec_command('sudo apt install docker-ce -y')
stdin, stdout, stderr = sshcon.exec_command("acidiag touch clean; y | reload")
time.sleep(10)
stdin, stdout, strerr = sshcon.exec_command('sudo apt update')

stdin, stdout, strerr = sshcon.exec_command('sudo apt-get install docker-compose-plugin')
stdin, stdout, stderr = sshcon.exec_command("acidiag touch clean; '[ENTER]' | reload")
stdin, stdout, stderr = sshcon.exec_command('docker run -d \\\
--name wireguard \\\
--cap-add=NET_ADMIN \\\
--cap-add=SYS_MODULE \\\
-e PUID=1000 -e PGID=1000 \\\
-e TZ=Europe/London \\\
-e SERVERURL=158.160.26.139 \\\
-e PEERS=laptop,tablet,phone \\\
-e PEERDNS=auto \\\
-p 51820:51820/udp \\\
-v wireguard_config:/config \\\
-v /lib/modules:/lib/modules \\\
--sysctl="net.ipv4.conf.all.src_valid_mark=1" \\\
--restart=unless-stopped \\\
linuxserver/wireguard')
sshcon.close()



