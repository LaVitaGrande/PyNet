from getpass import getpass
from connection_builder import builder
from pprint import pprint

print("Please enter the password:")
password = getpass()

devices = builder('hosts.json', password)

for name, values in devices.items():
    if values['conn']:
        print(name + " is ready")
    else:
        print(name + " has no connection")

