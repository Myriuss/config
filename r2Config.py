import getpass
import telnetlib

HOST = "192.168.122.22"
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

tn.write(b"int FastEthernet0/0.2\n")
tn.write(b"encapsulation dot1Q 2\n")
tn.write(b"ip add 192.168.22.0\n")
tn.write(b"no shut\n")

tn.write(b"int FastEthernet0/0.3\n")
tn.write(b"encapsulation dot1Q 3\n")
tn.write(b"ip add 192.168.33.0\n")
tn.write(b"no shut\n")

tn.write(b"int FastEthernet0/0.4\n")
tn.write(b"encapsulation dot1Q 4\n")
tn.write(b"ip add 192.168.44.0\n")
tn.write(b"no shut\n")

tn.write(b"end\n")
tn.write(b"exit\n")


print(tn.read_all().decode('ascii'))