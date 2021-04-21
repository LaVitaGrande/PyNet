from netmiko import ConnectHandler as ch
from getpass import getpass

connection = ch(
    host='cisco4.lasthop.io',
    username='pyclass',
    password=getpass(),
    device_type='cisco_ios',
    session_log='connection.txt',
)

print(connection.find_prompt())

