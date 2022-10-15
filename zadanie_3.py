s1 = input()
s2 = input()

n = len(s1)
m = len(s2)

if n == m:
    if n % 2 == 0:
        print('2')
    elif n % 3 == 0:
        print('3')
    else:
        print('0')
else:
    print('0')