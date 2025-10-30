"""
6 - Using the song “10 green bottles”, 
display the lines “There are [num] green bottles hanging on the wall, 
[num] green bottle hanging on the wall, and is 1 green bottle should accidentally fall”. 

Then ask the question “how many green bottles will be hanging on the wall?” 

If the user answers correctly, 
display the message “There will be [num] green bottles hanging on the wall”. 

If they answer incorrectly, 
display the message “No, try again” until they get it right. 

When the number of green bottles gets down to 0, 
display the message “There are no more green bottles hanging on the wall”.
"""

bottles = 3



while bottles > 0:
    print(f"There are {bottles} green bottles hanging on the wall,")
    print(f"{bottles} green bottle hanging on the wall, ")
    print(f"and is 1 green bottle should accidentally fall.")

    num = int(input("How many green bottles will be hanging on the wall? "))
    
    if num == bottles - 1:
        print(f"There will be {bottles -1} green bottles hanging on the wall")
        break
    else: 
        bottles -= 1
        print("No, try again")
    
    print("There are no more green bottles hanging on the wall")
        



'''
There are 1 green bottles hanging on the wall,
1 green bottle hanging on the wall,
and is 1 green bottle should accidentally fall.
How many green bottles will be hanging on the wall? 9
No, try again
There are no more green bottles hanging on the wall
--------------------------
There are 3 green bottles hanging on the wall,
3 green bottle hanging on the wall,
and is 1 green bottle should accidentally fall.
How many green bottles will be hanging on the wall? 2
There will be 2 green bottles hanging on the wall
'''
    
