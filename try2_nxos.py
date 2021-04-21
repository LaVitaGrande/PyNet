from netmiko import ConnectHandler
from getpass import getpass

connections = {}
devices = { 
    "nxos1.lasthop.io" : {
        "username" : 'pyclass',
        "password" : getpass(),
        "device_type" : 'cisco_nxos',
        "session_log" : 'connection.txt',
    },
    "nxos2.lasthop.io" : {
        "username" : 'pyclass',
        "password" : getpass(),
        "device_type" : 'cisco_nxos',
    }
}

for key, val  in devices.items():
    connections[key]=(ConnectHandler(host = key, **val))

for connection, _  in connections.items():
    print(connections[connection].find_prompt())

connections["nxos1.lasthop.io"].send_command("show version")
