product = {
    "description": "WCG E-Book",
    "price": 2.75,
    "sold": 1500,
    "stock": 5700
}


def sell(p):
    update = {"sold": p.get("sold", 0) + 1, "stock": p.get("stock") - 1}
    p.update(update)


def print_product(p):
    print(", ".join(["{}: {}".format(str(k), str(product[k])) for k in sorted(p.keys())]))

print_product(product)
for i in range(0, 100):
    sell(product)
print_product(product)
