constants = {"pi": 3.14, "e": 2.71, "root": 1.41}
print(constants)
constants["e"] = 2.80
print(constants)

"""
{'pi': 3.14, 'e': 2.71, 'root': 1.41}
{'pi': 3.14, 'e': 2.8, 'root': 1.41}
"""

colours = {1: "red", 2: "blue", 3: "green"}
print(colours)
colours[3] = "purple"
print(colours)

"""
{1: 'red', 2: 'blue', 3: 'green'}
{1: 'red', 2: 'blue', 3: 'purple'}
"""