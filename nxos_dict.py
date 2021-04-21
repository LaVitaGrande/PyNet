from netmiko import ConnectHandler as ch
from getpass import getpass

connections = []

devices = [
    {
        "host" : 'nxos1.lasthop.io',
        "username" : 'pyclass',
        "password" : getpass(),
        "device_type" : 'cisco_nxos',
        "session_log" : 'connection.txt',
    },
    {
        "host" : 'nxos2.lasthop.io',
        "username" : 'pyclass',
        "password" : getpass(),
        "device_type" : 'cisco_nxos',
    }
]

for dev in devices:
    connections.append(ch(**dev))

for connection in connections:
    print(connection.find_prompt())

connections[0].send_command("show version")

