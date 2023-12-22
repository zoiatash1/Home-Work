def fizz_buzz(n):
    for x in range(1, n+1):
        if x % 3 == 0 and x % 5 == 0:
           print('Fizz_buzz')
        elif x % 3 == 0:
            print('Fizz')
        elif x % 5 == 0:
            print('Buzz')
        else:
            print(x)

n = 17
fizz_buzz(n)
