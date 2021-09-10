# Prefix List Var or Command Generator
Build prefix lists of various lengths with random RFC1918 IP addresses

## Install
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Help
python generate_prefix_lists.py -h

## Usage Examples
python generate_prefix_lists.py 30000 RANDOMHOSTS1 ansible
python generate_prefix_lists.py 5 RANDOMHOSTS1 set

## Output
Script uses Jinja 2 templates to generate output. Either Into a YAML file for consumption by Ansible or as a text file with set commands that can be pasted into Junos.
