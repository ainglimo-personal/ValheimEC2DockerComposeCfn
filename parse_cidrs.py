import json

with open("./cidrs.json", "r") as json_file:
    content_dict = json.load(json_file)

print(content_dict['createDate'])

yamlstring = ""
for prefix in content_dict['prefixes']:
    if prefix['service'] == "EC2_INSTANCE_CONNECT":
        yamlstring += f"""\n{prefix['region']}:
\tCIDR: {prefix['ip_prefix']}"""

print(yamlstring)