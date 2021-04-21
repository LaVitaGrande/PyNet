from netmiko import ConnectHandler as ch
from getpass import getpass

device = { 
    "host" : 'nxos2.lasthop.io',
    "username" : 'pyclass',
    "password" : getpass(),
    "device_type" : 'cisco_nxos',
#    session_log='connection.txt',
}

connection = ch(**device)
print(connection.find_prompt())
