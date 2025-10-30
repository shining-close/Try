x = 10

def foo():
    x = 5
    print(f"Inside function, x = {x}")

foo()
print(f"Outside function, x = {x}")

"""
Inside function, x = 5
Outside function, x = 10
"""