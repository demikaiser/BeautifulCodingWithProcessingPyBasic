variable = {"Apple": 1, "Orange": 2, "Banana": 3}
print(type(variable))
print(len(variable))
print(variable["Apple"])
print(variable.get("Apple"))

print(variable.keys())
print(variable.values())
print(variable.items())

variable["Melon"] = 4
variable.pop("Melon")


