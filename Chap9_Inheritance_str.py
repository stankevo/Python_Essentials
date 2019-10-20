class RevStr(str):
    def __str__(self):
        return self[::-1]

def main():
    h = RevStr('Hello World!')
    print(h)

if __name__ == '__main__': main()
