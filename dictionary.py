def add_element(dict, key, value):
    if key not in dict:
        dict[key] = []
    dict[key].append(value)
    return dict




