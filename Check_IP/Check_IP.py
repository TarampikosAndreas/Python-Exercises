import socket

ip = input('Enter an IP Address :')

try:
        socket.inet_aton(ip)
        print("Valid IP")
except socket.error:
        print("Not Valid IP")
