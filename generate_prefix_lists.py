import ipaddress, random, argparse
from jinja2 import FileSystemLoader,Environment

def generate_vars_file(prefix_list, prefix_list_name, prefix_template):
    '''Generate Vars file from Jinja2 Template and Prefix Host List'''
    file_loader = FileSystemLoader('prefix_templates')
    env = Environment(loader=file_loader)
    prefix_template = env.get_template(prefix_template)
    prefix_output = prefix_template.render(prefix_list=prefix_list, prefix_list_name=prefix_list_name)
    with open('./generated_prefix_vars_files/prefix_vars.yml', 'w') as f:
        f.write(prefix_output)

def generate_host_list(host_count):
    '''Build list from RFC1918 addresses at random with the amount determined by the user'''
    list_of_as = list(ipaddress.ip_network('10.0.0.0/8').hosts())
    list_of_bs = list(ipaddress.ip_network('172.16.0.0/12').hosts())
    list_of_cs = list(ipaddress.ip_network('192.168.0.0/16').hosts())
    list_of_rfc1918 = list_of_as + list_of_bs + list_of_cs
    random_hosts = []
    for item in range(1, host_count):
        random_hosts.append(str(random.choice(list_of_rfc1918)))
    return random_hosts

if  __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate random prefix var list for Ansible')
    parser.add_argument('host_count', type=int, help="Amount of random hosts you want")
    parser.add_argument('prefix_list_name', type=str, help="Name of prefix list")
    parser.add_argument('template_type', type=str, help="Ansible or Set Command Template Types")
    args = parser.parse_args()
    host_count = args.host_count
    prefix_list_name = args.prefix_list_name
    prefix_template_type = args.template_type
    if prefix_template_type == 'ansible':
        prefix_template = 'prefix_var_template.j2'
    elif prefix_template_type == 'set':
        prefix_template = 'prefix_var_set_commands.j2'
    else:
        print('Pick a valid template type, ansible or set')
    prefix_list = generate_host_list(host_count)
    generate_vars_file(prefix_list, prefix_list_name, prefix_template)
