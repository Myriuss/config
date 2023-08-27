import getpass
import telnetlib

HOST = "192.168.1.2"
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

tn.write(b"int FastEthernet0/0\n")
tn.write(b"no shut\n")

#192.168.2.1 f0/0
tn.write(b"int FastEthernet2/0.5\n")
tn.write(b"encapsulation dot1Q 5\n")
tn.write(b"ip add 192.168.55.0 255.255.255.0\n")
tn.write(b"no shut\n")

tn.write(b"int FastEthernet2/0.6\n")
tn.write(b"encapsulation dot1Q 6\n")
tn.write(b"ip add 192.168.66.0 255.255.255.0\n")
tn.write(b"no shut\n")

tn.write(b"int FastEthernet1/0\n")
tn.write(b"ip add 192.168.7.0 255.255.255.0\n")
tn.write(b"no shut\n")

tn.write(b"end\n")
tn.write(b"exit\n")


print(tn.read_all().decode('ascii'))