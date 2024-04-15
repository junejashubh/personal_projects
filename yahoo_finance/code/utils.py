import yaml

def replace_placeholders(d, base_dict=None):
    if base_dict is None:
        base_dict = d.copy()
    for key, value in d.items():
        if isinstance(value, str):
            d[key] = value.format(**base_dict)
            base_dict[key] = d[key]
        elif isinstance(value, dict):
            d[key] = replace_placeholders(value,base_dict)
    return d
    

def read_config(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    config = replace_placeholders(config)
    return config