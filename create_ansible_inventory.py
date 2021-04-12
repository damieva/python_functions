import sys, json

def create_inventory(inventory):
    result = '---\n'
    identation= ''
    for group in inventory:
        if group.get("name") == "all":
            result += "all:\n"
            identation= '    '
            if "hosts" in group:
                result += "  hosts:\n"
                for host in group.get("hosts"):
                    result += "    " + host + ":" + "\n"
            if "vars" in group:
                result += "  vars:\n"
                for key, value in group.get("vars").items():
                    result += "    " + key + ":" + value + "\n"
            result += "  children:\n"
        else:
            result += identation + group.get("name") + ":" + "\n"
            result += identation + "  hosts:\n"
            for host in group.get("hosts"):
                result += identation + "    " + host + ":" + "\n"
            if "vars" in group:
                result += identation + "  vars:\n"
                for key, value in group.get("vars").items():
                    result += identation + "    " + key + ":" + value + "\n"
    return result




inventory = [
    {
        "name": "all",
        "hosts": ["120.0.0.1", "192.168.1.195"],
        "vars": {
            "python_version": "3.5.2"
        }
    },
    {
        "name": "web_servers",
        "hosts": ["10.23.0.12", "192.168.1.195"],
        "vars": {
            "ssh_root_pass": "{{ root_pass }}"
        }
    },
    {
        "name": "db_servers",
        "hosts": ["10.23.0.18", "192.168.1.89"],
        "vars": {
            "ssh_root_user": "{{ root_user }}"
        }
    }
]

inventory_2 = [
    {
        "name": "web_servers",
        "hosts": ["10.23.0.12", "192.168.1.195"],
        "vars": {
            "ssh_root_pass": "{{ root_pass }}"
        }
    },
    {
        "name": "db_servers",
        "hosts": ["10.23.0.18", "192.168.1.89"],
        "vars": {
            "ssh_root_user": "{{ root_user }}"
        }
    }
]


file = open("inventory.txt", "r")

contents = file.read()

print(contents)

#print(create_inventory(inventory_2))
#print(sys.argv[1])
