EXAMPLE_DICT = {
    "animals": ["dog", "cat", "fish"],
    "a_number": 1,
    "a_name": "Sebastián",
    "a_boolean": True,
    "another_dict": {
        "you could": "keep going",
        "like this": "forever"
    }
}


def print_key(dictionary, key):
    print(str(dictionary.get(key, "Key was not found")))

# Create a key
EXAMPLE_DICT[
    "this_one_does_not_exist"] = "it exists now"  # This statement will create the key "this_one_does_not_exist"
# and assign to it the value "it exists now"
print_key(EXAMPLE_DICT, "this_one_does_not_exist")

# Update a key
EXAMPLE_DICT["a_boolean"] = False  # Exactly, it looks the same, and behaves the same. It just overwrites the given key.
print_key(EXAMPLE_DICT, "a_boolean")

# Delete a key
del EXAMPLE_DICT["this_one_does_not_exist"]  # Now "this_one_does_not_exist" ceased from existing (Again).
print_key(EXAMPLE_DICT, "this_one_does_not_exist")