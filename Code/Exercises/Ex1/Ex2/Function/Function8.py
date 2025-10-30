"""
8 - 
Create a programme that will allow the user to easily manage a list of names. 
You should display a menu that will allow them to 
add a name to the list, 
change the name in the list, 
delete a name from the list or 
view all the names in the list. 

There should be a menu option to allow the user to end the programme. 

If they select an option that is not relevant, 
then it should display a suitable message. 

After they have made a selection to either, add a name, change a name, delete a
name or view all the names, 
they should see the menu again without having to restart the programme. 
The programme should be as easy to use as possible.
"""

name_list = ["Alex", "Kelvin"]

def addName(n):
    name_list.append(n)
    print("\n")

def changeName(n, n_new):
    if n in name_list:
        name_list[name_list.index(n)] = n_new
        print("\n")
    else:
        print(f"There is no one named '{n_new}'\n")

def deleteName(n):
    if n in name_list:
        del name_list[name_list.index(n)]
        print("\n")
    else:
        print(f"There is no one named '{n}'\n")

def viewAllNames():
    print("All the names are: ")
    print(name_list, "\n")

def main():

    print("There are five operations:")
    print("viewAll, delete, change, add, blank to quit")

    operation = input("Which operation you want to do? \n")

    while operation != "":
        if operation == 'viewAll':
            viewAllNames()
            operation = input("Which operation you want to do next? \n")
        elif operation == 'delete':
            name = input("which name to delete: ")
            deleteName(name)
            operation = input("Which operation you want to do next? \n")
        elif operation == 'change':
            name = input("Which name to change: ")
            new_name = input("The new name: ")
            changeName(name, new_name)
            operation = input("Which operation you want to do next? \n")
        elif operation == 'add':
            name = input("The name to add: ")
            addName(name)
            operation = input("Which operation you want to do next? \n")

if __name__ == "__main__":
    main()







