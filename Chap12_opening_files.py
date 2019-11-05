def main():
    f = open("/Users/elena/repo/Python/Python_Essentials/Exercise Files/Chap12/lines.txt")
    for l in f:
        print(l.strip())

    f1 = open('/Users/elena/Desktop/NewFile.txt', 'w') ## to create a new file
    
if __name__ == '__main__': main()