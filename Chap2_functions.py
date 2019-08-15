def is_prime(n):
    if n <= 1:
        return False
    for x in range(2,n):
        if (n % x == 0):
            return False
    else:
        return True


def list_all_primes(a = 100):
    for i in range(2, a):
        if is_prime(i) == True:
            print(i, end = ' ', flush = True)
    print()

z = 97
if is_prime(z):
    print('{} is prime.'.format(z))
else:
    print('{} is not prime.'.format(z))
    print('Prime numbers are:')
    list_all_primes(z)
