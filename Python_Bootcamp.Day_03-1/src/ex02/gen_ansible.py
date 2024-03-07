import yaml
import os

file_dir = os.path.dirname(__file__)
file_name = os.path.join(file_dir, '../../materials/todo.yml')
dir_ex00 = os.path.join(file_dir, '../ex00/')
dir_ex01 = os.path.join(file_dir, '../ex01/')
dir_src = os.path.join(file_dir, '../')
with open(file_name, 'r') as fh:
    data = yaml.load(fh, Loader=yaml.FullLoader)

res = {"name": "Ansible Playbook", 'hosts': "localhost", 'become': "yes", "tasks": []}
for package in data['server']['install_packages']:
    res["tasks"].append({"ansible.builtin.apt": {'name': package}})

for file in data['server']['exploit_files']:
    res["tasks"].append({"ansible.builtin.copy": {"src": f"{dir_ex00 if file == 'exploit.py' else dir_ex01}{file}",
                                                  "dest": f"{file_dir}/{file}", "follow": "yes"}})

for file in data['server']['exploit_files']:
    if file == "consumer.py":
        args = "-e " + ",".join(data['bad_guys'])
        cmd = f"python3 {file} {args}"
    else:
        cmd = f"python3 {file}"

    res["tasks"].append({"ansible.builtin.shell": {"cmd": f"{cmd}"}})

with open("deploy.yml", 'w') as f:
    yaml.dump([res], f, default_flow_style=False)
