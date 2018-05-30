#Scipt goes into a specified network and does a ping test, checks DNS entry, checks SSH login and reports back the results in a CSV file


import socket
import subprocess
import netifaces
import csv
import paramiko
  
def checkPING(IP):
    try:
        ping = subprocess.check_output(['ping', '-c1', ip])
        return "Host is UP"
    except:
        return "Host is DOWN"
  
def checkDNS(IP):
    try:
        dns = socket.gethostbyaddr(ip)
        return dns[0]
    except:
        return "No DNS entry found"
  
def checkSSH(IP):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username='root', password='Password!')
        ssh.close()
        return "SSH OK"
    except:
        return "SSH NO"
  
ip_list = []
dns_list = []
status_list = []
ssh_list = []
  
csvfile= open('file.csv', 'w')
for loop_ip in range (30):
    ip = '10.0.0.%d' % loop_ip
    print ip, checkDNS(ip), checkPING(ip),checkSSH(ip)
    data = ip+" ",checkDNS(ip)+" ",checkPING(ip)+" ",checkSSH(ip)
    #data_list.append(data)
    ip_list.append(ip)
    dns_list.append(checkDNS(ip))
    status_list.append(checkPING(ip))
    ssh_list.append(checkSSH(ip))
#print data_list
writer = csv.writer(csvfile, dialect='excel')
writer.writerows(zip(ip_list, dns_list, status_list, ssh_list))
