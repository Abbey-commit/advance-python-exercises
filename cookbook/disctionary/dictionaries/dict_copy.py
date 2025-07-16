me = {
    "name": {
        "first": "Sebastián",
        "last": "Vinci"
    },
    "age": 21
}
my_clone = me.copy()

my_clone["age"] = 22
print("my age: {}, my clone's age: {}".format(me.get("age"), my_clone.get("age")))

my_clone.get("name")["first"] = "Michael"
print("my name: {}, my clone's name: {}".format(me.get("name").get("first"), my_clone.get("name").get("first")))
