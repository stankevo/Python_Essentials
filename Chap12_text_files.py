def main():
    infile = open('/Users/elena/repo/Python/Python_Essentials/Exercise Files/Chap12/lines.txt', 'rt')
    outfile = open('/Users/elena/repo/Python/Python_Essentials/Chap12_files/lines-copy.txt', 'wt')
    for i in infile:
        print(i.strip(), file=outfile)
        #outfile.writelines(i) #another option
        print('.', end=' ', flush=True)
    outfile.close()
    print('\nCopying is done')


if __name__ == '__main__': main()