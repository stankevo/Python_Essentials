import platform

def main():
    message()

def message():
    print('This is Python version {}'.format(platform.python_version())); print('line 2')
print('line 3')

if __name__ == '__main__': main()
