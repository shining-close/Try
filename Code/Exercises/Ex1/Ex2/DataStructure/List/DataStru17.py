"""17 - Write a programme that asks the user to enter the names of three people they want to invite to
a party and store them in a list. 

After they have entered all three names, ask them if they want to add another. 
If they do, allow them to add more names until they say “no”. 

When they say “no”, display how many people they have invited to the party"""

name_list = []

name_list = input("Three names: ").split()

select = input("Want to enter a new name? (yes/no) ").lower()

while select != 'no':
    name = input("The new name: ")
    name_list.append(name)
    select = input("Want to enter another name? (yes/no) ").lower()

print(f"Totally entered {len(name_list)} names.")

'''
Three names: Bob Alex Kelvin
Want to enter a new name? (yes/no) yes
The new name: Harley
Want to enter another name? (yes/no) yes
The new name: Henry
Want to enter another name? (yes/no) no
Totally entered 5 names.
'''