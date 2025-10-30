
def calculate_area(length, width):
    area = length * width
    print(f"Area inside function: {area}")
    return area

area = 0

def main():
    area = calculate_area(5, 3)
    print(f"Area in main after calculation:{area}")

    area = 7
    print(f"New value assigned to area in main: {area}")


# 使用__name__ == "__main__"
# 这个机制让 Python 脚本既能作为独立程序运行，又能作为模块被导入，是 Python 模块化编程的重要特性。
# 这部分代码只有在直接运行 GlobalVariable2.py 时才会运行
# 1.在终端 python GlobalVariable2.py
# 2.作为脚本导入，在另一个.py文件中，例：main.py
#   使用 import GlobalVariable2
#        GlobalVariable2.calculate_area()
if __name__ == "__main__":
    main()

print(f"Global area after mian execution: {area}")


# if __name__ == "__main__": 的作用
# 这个条件判断的主要作用是区分当前模块是被直接运行还是被导入，从而控制某些代码的执行方式。
# 1. 直接运行脚本时（python script.py）
#   __name__ 的值是 "__main__"，所以 if 块内的代码会执行。
#   通常用于定义脚本的主逻辑，比如测试代码、启动函数等。

# 2. 被其他模块导入时（import script）
#   __name__ 的值是模块名（如 "script"），所以 if 块内的代码不会执行。
#   这样可以避免导入时自动执行不必要的代码，仅提供函数、类等定义。

# 为什么需要这个判断？
# 1.防止导入时执行测试代码
#  如果模块中有测试代码（如 print()、函数调用等），直接导入会导致这些代码自动运行，可能影响主程序逻辑。
#  使用 if __name__ == "__main__": 可以避免这个问题。

# 2.模块化开发
#  在大型项目中，某些模块既可以被其他模块导入使用，也可以单独运行（比如测试功能）。
#  if __name__ == "__main__": 让模块更加灵活。

# 3.提高代码复用性
#  如果模块被导入，它只提供函数/类定义，而不会执行额外的操作，使得代码更干净、更易于管理。