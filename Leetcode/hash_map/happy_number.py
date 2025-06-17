class Solution(object):
    def isHappy(self, n):
        seen = []
        while n != 1 :
            if n in seen:
                return False
            seen.append(n)

            total = 0 
            while n > 0 :
                last_digit = n % 10
                total += last_digit ** 2
                n = n // 10
            
            n = total
        return True
    
sol = Solution()
print(sol.isHappy(19))