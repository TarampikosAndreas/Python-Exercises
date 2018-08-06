import re

ip = input("Type an IP Address: ")

aa = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip)


if aa:
    ip = aa.group()
    print("Valid IP")
else:
    print("Not Valid IP")
