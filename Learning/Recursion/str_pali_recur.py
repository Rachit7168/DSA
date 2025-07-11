def func(s , right = 0 ,left = 0 ):
    if not isinstance(s , str):
        raise TypeError("Input must be a string")
    if right == 0:
        right = len(s) - 1
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return func(s , left + 1 , right - 1)
    
print(func(s="rachitihcar"))