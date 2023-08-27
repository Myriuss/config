import telnetlib
import time

HOST = "192.168.208.1"  # Adresse IP du commutateur
USER = "sw0"  
PASSWORD = "password"  

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(USER.encode('ascii') + b"\n")

tn.read_until(b"Password: ")
tn.write(PASSWORD.encode('ascii') + b"\n")

tn.read_until(b">")  # Ou d'autres prompts selon votre commutateur

# Entrez en mode de configuration
tn.write(b"enable\n")
tn.read_until(b"Password: ")
tn.write(PASSWORD.encode('ascii') + b"\n")
tn.read_until(b"#")

# Commandes de configuration
commands = [
    b"conf t",
    b"banner motd #Unauthorized access to this device is prohibited!#",
    b"interface vlan1",
    b"ip address  192.168.10.1 255.255.255.0",
    b"no shutdown",
    b"exit",
    b"vlan 10",
    b"name vlan10",
    b"exit",
    b"int vlan 10",
    b"ip address  192.168.10.1 255.255.255.0",
    b"no shut",
    b"vlan 2",
    b"name vlan2",
    b"exit",
    b"int vlan 2",
    b"ip address  192.168.2.1 255.255.255.0",
    b"no shut",
    b"exit",
    b"vlan 3",
    b"name vlan 3",
    b"exit",
    b"int vlan 3",
    b"ip address  192.168.3.1 255.255.255.0",
    b"no shut",
    b"exit",
    b"int range fa0/1-2",
    b"switchport mode access",
    b"switchport access vlan 10",
    b"exit",
    b"int range fa0/3-5",
    b"switchport mode access",
    b"switchport access vlan 2",
    b"exit",
    b"int range fa0/6-8",
    b"switchport mode access",
    b"switchport access vlan 3",
    b"exit",
    b"int fa0/10",
    b"switchport mode trunk",
    b"description LINK-TO-ROUTER",
    b"exit",
    
]

for cmd in commands:
    tn.write(cmd + b"\n")
    time.sleep(1)  # Attendre un peu entre chaque commande

output = tn.read_all().decode('ascii')
print(output)

tn.close()
