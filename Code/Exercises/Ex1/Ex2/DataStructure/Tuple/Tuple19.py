"""
19 - Create a tuple containing the names of five countries and display the whole tuple. 

Ask the user to enter one of the countries that have been shown to them 
and then display the index number (i.e. position in the list) of that item in the tuple.
Next, the programme should ask the user to enter a number (index) and display the country in that position.
"""

countries_tuple = ("UK", "USA", "Japan", "China", "New Zealand")

print("The whole tuple are: ", countries_tuple)

country = input("Enter a country in this tuple: ")

print(f"The index of {country} is {countries_tuple.index(country) + 1}")

num = int(input("Enter a country's num: "))

print(f"The country is {countries_tuple[num - 1]}")

'''----------upgrade-----------'''

countries = input("Enter five countries: ").split("," + " ")
print(tuple(countries))
countries_dict = {}
for i in range(0, len(countries)):
    countries_dict[countries[i]] = i + 1
print(countries_dict)