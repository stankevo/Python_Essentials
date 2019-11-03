print('Hello, World!')
print('Hello, World!'.upper())
print('Hello, World!'.swapcase())
print("""
Hello,
World!

{}
""".format(13*11))

class MyString(str):
    def __str__(self):
        return self[::-1]

s = MyString('Hello, World!')
print(s)

