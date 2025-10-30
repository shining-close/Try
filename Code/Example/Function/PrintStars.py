rows = int(input("Enter the rows:"))

for i in range(rows):
    spaces = " " * (rows - i -1)
    stars = "*" * (2 * i + 1)
    print(f"{spaces}{stars}".rstrip())



# 在 Python 中，strip()、lstrip() 和 rstrip() 是用于处理字符串的三个常用方法，
# 它们的作用都是去除字符串两端的空白字符或指定字符，但它们的去除位置有所不同.
# strip()：去除字符串两端的空白字符或指定字符。
# lstrip()：去除字符串左边（开头）的空白字符或指定字符。
# rstrip()：去除字符串右边（结尾）的空白字符或指定字符。
# 这些方法不会改变原字符串，而是返回一个新的字符串。

#######################
#strip()方法用于去除字符串两端的空白字符
# （默认情况下，包括空格、换行符、制表符等），或者去除指定的字符序列
# 去除两端的空白字符
text = "  Hello, World!  "
cleaned_text = text.strip()
print(cleaned_text)  # 输出: "Hello, World!"
 
# 去除指定的字符
text = "xxxyHello, World!yyy"
cleaned_text = text.strip('xy')
print(cleaned_text)  # 输出: "Hello, World!"

########################
# lstrip() 方法用于去除字符串左边（开头）的空白字符或指定的字符。
# 去除左边的空白字符
text = "  Hello, World!  "
cleaned_text = text.lstrip()
print(cleaned_text)  # 输出: "Hello, World!  "
 
# 去除左边的指定字符
text = "xxxyHello, World!yyy"
cleaned_text = text.lstrip('xy')
print(cleaned_text)  # 输出: "Hello, World!yyy"

#########################
# rstrip() 方法用于去除字符串右边（结尾）的空白字符或指定的字符。

# 去除右边的空白字符
text = "  Hello, World!  "
cleaned_text = text.rstrip()
print(cleaned_text)  # 输出: "  Hello, World!"
 
# 去除右边的指定字符
text = "xxxyHello, World!yyy"
cleaned_text = text.rstrip('xy')
print(cleaned_text)  # 输出: "xxxyHello, World!"
