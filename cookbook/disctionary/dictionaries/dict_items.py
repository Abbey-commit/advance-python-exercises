def print_dict(dictionary):
    for k, v in dictionary.items():
        print("{}: {}".format(str(k), str(v)))


example = {
    "name": "Sebastián",
    "last_name": "Vinci",
    "age": 21
}

print_dict(example)
