a = [1, 2, 3, 4, 5]
b= [1, 2, 3, 6, 7]
def findUnion(arr_1,arr_2):
    n = len(arr_1)
    m = len(arr_2)
    i ,j = 0 , 0
    result = []
    
    while i < n and j < m:
        if arr_1[i] <= arr_2[j]:
            if len(result) == 0 or result[-1] != arr_1[i]:
                result.append(arr_1[i])
            i += 1
        else:
            if len(result) == 0 or result[-1] != arr_2[j]:
                result.append(arr_2[j])
            j += 1
        
    while i < n:
        if len(result) == 0 or result[-1] != arr_1[i]:
            result.append(arr_1[i])
        i += 1
            
    while j < m:
        if len(result) == 0 or result[-1] != arr_2[j]:
            result.append(arr_2[j])
        j += 1
    return result

print(findUnion(a ,b))
