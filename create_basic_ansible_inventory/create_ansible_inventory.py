import sys, json, jinja2

def create_basic_inventory(*args):
# Extract hosts:
    hosts = args[0].split("=")[1].split(",")
    print(hosts)

# Extract vars:
    vars={}
    for arg in args[1:]:
        vars[arg.split("=")[0]] = arg.split("=")[1]
    print(vars)

# Creating jinja Environment
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    templateEnv.filters['jsonify'] = json.dumps
    template = templateEnv.get_template('inventory_template.yml')
    page = {
        'hosts': hosts,
        'vars': vars
    }
# Mapping key:value page vble to template and writing in a file
    f = open("../inventory.yml", "w")
    f.write(template.render(page=page))
    f.close()

if __name__ == "__main__":
    create_basic_inventory(*sys.argv[1:])