my_dict = {
    "name": "Sebastián",
    "age": 21
}


def keys(dictionary):
    result = [k for k in dictionary]
    # result.append("break the program plz")
    if len(result) != len(dictionary):
        raise Exception('expected {} keys. got {}'.format(len(dictionary), len(result)))
    return result


print(str(keys(my_dict)))
