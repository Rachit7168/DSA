from math import sqrt
class Solution(object):
    def isThree(self, num):
        result = []
        for i in range(1 , int(sqrt(num)) + 1):
            if num % i == 0:
                result.append(i)
                if num // i != i:
                    result.append(num//i)
        if len(result) == 3:
            return True
        else: 
            return False
        