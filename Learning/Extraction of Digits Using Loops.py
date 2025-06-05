def extraction(n):
    num = n
    while num > 0:
        last_digit = num % 10
        print(last_digit)
        num = num//10
number = 7535
extraction(n=number)