list1 = [5 , 3 , 2 , 2 , 1 , 5 , 5 , 7 , 5 , 10]
m = [10 , 111 , 1 , 9 , 5 , 67 , 2]

hash_map = {}
for i in range(0 , len(list1)):
    hash_map[list1[i]] = hash_map.get(list1[i],0) + 1
for i in m:
    print(f"{i} appears" , hash_map.get(i , 0) , "times")