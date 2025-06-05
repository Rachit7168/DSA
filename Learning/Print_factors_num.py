# TODO : Brute Force method
def brute_force(num):
    result = []
    for i in range(1 , num + 1):
        if num % i == 0:
            result.append(i)
    return result


# TODO : Better Solution
def better_sol(num):
    result = []
    for i in range(1 , num // 2 + 1):
        if num % i == 0 :
            result.append(i)
    result.append(num)
    return result


# TODO : Optimized Sol
from math import sqrt
def optimized_sol(num):
    result = []
    for i in range(1 , int(sqrt(num)) + 1):
        if num % i== 0:
            result.append(i)
            if num // i != i:
                result.append(num//i)
    result.sort()
    return result