#let number plus from 0 until the total number is larger than 100

total = 0

while total < 100:
    number = int(input("Enter a number: "))   
    total = total + number
    
    if total <= 100:
        print("The total is less than 100.")
        print("The total is: ", total, "\n")
    else:
        print("The total is larger than 100.")
        print("Hello, the total is: ", total)

    

