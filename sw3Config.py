import getpass
import telnetlib

HOST = "192.168.5.33"
user = input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Usernmae: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"ls\n")
tn.write(b"password\n")
tn.write(b"conf t\n")

tn.write(b"vlan 7\n")
tn.write(b"name vlan7\n")
tn.write(b"no shut\n")
tn.write(b"exit\n")
tn.write(b"interface range Ethernet 0/1-2\n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 7\n")
tn.write(b"exit\n")

tn.write(b"vlan 8\n")
tn.write(b"name vlan8\n")
tn.write(b"no shut\n")
tn.write(b"exit\n")
tn.write(b"interface Ethernet 0/3\n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 8\n")
tn.write(b"exit\n")
tn.write(b"interface Ethernet 1/0\n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 8\n")
tn.write(b"exit\n")

tn.write(b"interface Ethernet 0/0\n")
tn.write(b"description LINK-TO-ROUTER1\n")
tn.write(b"switchport mode trunk\n")
tn.write(b"exit\n")
tn.write(b"end\n")
tn.write(b"exit\n")


print(tn.read_all().decode('ascii'))