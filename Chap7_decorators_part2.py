import time

def main():
    big_sum(10000)
    factorial(10, 'We did it!')

def elapsed_time(f):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        f(*args)
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')
        print()
    return wrapper

@elapsed_time
def big_sum(n):
    numbers = range(n)
    sum = 0
    for i in range(n):
        sum += numbers[i]
    print(f'Sum of numbers from 1 to {n-1}: {sum}')

@elapsed_time
def factorial(n, word):
    numbers = range(1,n+1)
    mult = 1
    for i in range(n):
        mult = mult * numbers[i]
    print(f'{n}! = {mult}')
    print(f'second argument for this function is {word}')

if __name__ == "__main__": main()
        
