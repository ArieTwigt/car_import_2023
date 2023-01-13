import json

brands_str = input("Brands to import:\n")
brands_list = brands_str.split(" ")

config_dict = {}
config_dict['brands'] = brands_list

config_str =  json.dumps(config_dict)

with open("config.json", "w") as file:
    file.write(config_str)