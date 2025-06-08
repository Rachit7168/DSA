class Solution(object):
    def isPalindrome(self, n):
        num = n
        result = 0
        while num  > 0 :
            last_digit = num % 10
            result = (result * 10) + last_digit
            num = num//10
        return result == n