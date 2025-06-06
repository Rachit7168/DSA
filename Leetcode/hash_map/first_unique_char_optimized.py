def count(string):
    hash_map = {}
    for i in range(0 , len(string)):
        hash_map[string[i]] = hash_map.get(string[i], 0 ) + 1
    for i in range(len(string)):
        if hash_map[string[i]] == 1:
            return i
    return -1

string = "aabb"
print(count(string=string))

