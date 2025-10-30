def drawBox1():
    print("##########")
    print("&        +")
    print("&        +")
    print("**********")

# Parameter variable
# Such as width and fill are created when the function is called
# The for loop control variable (i) is created when the loops begins to execute

def drawBox2(width, height):

    if width < 4 or height < 4:
        print("Error: The width or height is too small")
        quit()

    print("*" * width)

    for i in range (height - 4):
        print("*" + " " * (width - 2) + "*")

    print("*" * width) 


def drawBox3(width, height, outline = "*", fill=" "):

    if width < 4 or height < 4:
        print("Error: The width or height is too small")
        quit()

    print(outline * width)

    for i in range (height - 4):
        print(outline + fill * (width - 4) + outline)

    print(outline * width)


drawBox2(20, 8)

drawBox3(20, 8) 
# If I don't use 123, it will default to the lastest drawBox() 

drawBox3(20, 8, "&", ".")