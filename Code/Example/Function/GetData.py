def get_data():
    username = input("Enter your user name: ")
    age = int(input("Enter your age: "))

    #combine the username and age together
    data_tuple = (username, age)

    return data_tuple

def message (username, age):
    if age <= 10:
        print("Hi", username)
    else:
        print("Hello", username)

def main():
    # This step get the username and age from get_data function
    # operate the first time
    username, age = get_data()

    # This step get the data_tuple from get_data function
    # Operate the second time
    username_age = get_data()

    print(username, "+", age)
    print(username_age)

    message(username, age)

main()

"""
Enter your user name: guan
Enter your age: 25
Enter your user name: liu
Enter your age: 9
guan + 25
('liu', 9)
Hello guan
"""