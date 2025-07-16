def print_dict(dictionary):
    ks = sorted(dictionary.keys())
    for k in ks:
        print("{}: {}".format(str(k), str(dictionary.get(k))))


example = {
    "name": "Sebastián",
    "last_name": "Vinci",
    "age": 21
}

print_dict(example)
