import json
from netmiko import ConnectHandler

def builder(file, password):
    with open(file) as hosts_file:
        hosts = json.load(hosts_file)

    for name, config in hosts.items():
        hosts[name]["conn"] = ConnectHandler(host = config["host"], username = config["username"], password = password, device_type = config["device_type"])

    return hosts

