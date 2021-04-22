import json
from getpass import getpass
from netmiko import ConnectHandler

print("Please enter the password:")
password = getpass()
connections = {}

with open('lab-hosts.json') as hosts_file:
    hosts = json.load(hosts_file)

for name, config in hosts.items():
    connections[name] = ConnectHandler(password = password, **config)

for name, connection in connections.items():
    print(name + " has hostname " + connection.find_prompt())

