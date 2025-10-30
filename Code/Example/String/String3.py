name = input("Enter your first name: ")

if len(name) < 5:
    sur_name = input("Enter your sur_name:")
    name = name+sur_name
    print(name.upper())
else:
    print(name.lower())