def main():
    infile = open('/Users/elena/repo/Python/Python_Essentials/Exercise Files/Chap12/berlin.jpg', 'rb')
    outfile = open('/Users/elena/repo/Python/Python_Essentials/Chap12_files/berlin.jpg', 'wb')
    while True:
        buf = infile.read(10240)
        if buf:
            outfile.write(buf)
            print('.', end=' ', flush=True)
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()