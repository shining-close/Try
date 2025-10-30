# index start from 0
# does not all have to be of the same type

our_list = [1, 2, [3, 4, 5], 6, 7, 8]

# list and dic is the changable type, diff_list2 and diff_list1 point to the same place
# When diff_list2 change, the diff_list1 also change
# But for the unchangable type like integer, strings and tuple, change num1 will not change num2
our_list2 = our_list[2]
our_list3 = our_list[2][0]

print(our_list)
print(our_list2)
print(our_list3)

print("\n")

num1 = 5
num2 = num1 
num2 = 10
print(f"The num1 is {num1}")
print(f"The num2 is {num2}")

print("\n")

# global variable
diff_list = [1, 'orange', [3, 4, 5], 6, 7, 8, 'blue', 1.4] 
print(f"The initial list diff_list is {diff_list}")    
diff_list1 = diff_list
diff_list1[1] = "green"
print(f"The diff_list1 is {diff_list1}")
print(f"Without def, the change in list1 will also change the list: {diff_list} \n")


def changeOneItem(list):
    diff_list2 = list
    print(f"After def the diff_list1 is {diff_list1}")
    diff_list2[1] = ["orange"]
    print(diff_list2)
    diff_list2[1] = "orange"
    print(diff_list2)
    print("\n")

# Add a new item in the end of the list
def addNew(diff_list1):
    diff_list3 = diff_list1
    diff_list3.append(input("Add another colour by using append: "))
    print(diff_list3)
    print(diff_list1)
    print("\n")

# Insert a new item in a certain position
def insertNew(diff_list1):
    diff_list4 = diff_list1
    diff_list4.insert(2, "This is a new insert")
    print(diff_list4)
    print("\n")

# Delete an item in a certain place
def deleteItem(diff_list1):
    diff_list5 = diff_list1
    print(diff_list5)
    del diff_list5[4]
    print(f"After delete: {diff_list5}")
    print("\n")


# Remove a certain item
def removeItem(diff_list1):
   diff_list6 = diff_list1
   print(diff_list6)
   diff_list6.remove("red")
   print(f"After remove: {diff_list6}")
   print("\n")

# Remove the last element 1.4
def popLast(list):
    diff_list = list.pop()
    print(diff_list)


def main():
    diff_list1 = [1, 'orange', [3, 4, 5], 6, 7, 8, 'blue', 1.4]
    changeOneItem(diff_list1)
    print(f"The diff_list1 is {diff_list1} \n")
    addNew(diff_list1)
    insertNew(diff_list1)
    deleteItem(diff_list1)
    removeItem(diff_list1)

if __name__ == "__main__":
    main()