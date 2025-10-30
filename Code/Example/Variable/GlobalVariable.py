# global variablr
count = 0

def increment1():
    global count # Declare that we want to modify the global variable
    count += 1   # This modifies the global state

# 在add函数中对count的修改并不会影响main函数中的k变量。
# 在add函数中，count被重新绑定为一个新的局部变量，它只是临时地覆盖了传入的k值，
# 但这个修改只在add函数的局部作用域内有效。
# 一旦add函数执行结束，这个局部变量count就会被销毁，而main函数中的count变量保持不变。
def increment2(number):
    number += 1   # This don't modify the global state

def increment3(number):
    return number + 1  
    
def main():
    print(f"Initial count: {count}")  # Should be 0
    increment1()   # This will change the global 'count'
    print(f"Count after increment1: {count}")   # Should be 1

    print("Display the count number:", count)

    increment2(count)
    print(f"Count after increment2: {count}")   # Should be 1


    local_count = 0
    print(f"Initial local count: {local_count}")   # Should be 0

    local_count = increment3(local_count)   #需要一个返回一个数，所以要有 return
    print(f"Local count after increment3: {local_count}")   # Should be 1

# wrong use:
    local_count = increment2(local_count)
    print(f"Local count after increment2: {local_count}")   # Should be 2 but is none

    

if __name__ == "__main__":
    main()