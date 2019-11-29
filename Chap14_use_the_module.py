import datetime
import saytime_my


def main():
    now =  datetime.datetime.now()
    try:        
        tw = saytime_my.timeToWord(now.time())
        print('Current time: ')
        print(tw)
    except TypeError as e:
        print(f'TypeError: {e}')

    print('\nTest time:')
    t1 = datetime.time(0,0)
    t2 = saytime_my.timeToWord(t1)
    print(t2)

    l = ((0, 0), (0, 1), (11, 0), (12, 0), (13, 0), (12, 29), (12, 30),
             (12, 31), (12, 15), (12, 30), (12, 45), (11, 59), (23, 15), 
             (23, 59), (12, 59), (13, 59)
            )

    tests = list()
    for i in l:
        tests.append(datetime.time(i[0], i[1]))

    for i in tests:
        print(f'{i} - {saytime_my.timeToWord(i)}')



if __name__ == '__main__': main()