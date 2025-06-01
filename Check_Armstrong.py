def check(n):
    num = n
    total = 0 
    nod = len(str(n)) # number of digits
    while num > 0 :
        last_digit = num % 10
        total = total + (last_digit ** nod)
        num = num // 10
    return n == total
print(check(n=1634))