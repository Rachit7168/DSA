# Code to count the frequency of all elements from a to z in the array.

name = 'Rachit'
vowels = ["a" , "e" , "i" , "o" , "u"]
hash_map=[0] * 27

for char in name:
    ascii_value = ord(char.lower()) # 97 - 122
    index = ascii_value - 97
    hash_map[index] += 1
    
for char in vowels:
    ascii_value = ord(char.lower()) # 97 - 122
    index = ascii_value - 97
    # print(f"The vowel {char} appears  {hash_map[index]} times")

#dict method

name = "Harsha"
vowels = ["a" , "e" , "i" , "o" , "u"]

hash_map = {}
for i in range(0 , len(name)):
    hash_map[name[i]] = hash_map.get(name[i] , 0) + 1
for char in vowels:
    print(f"The vovwel {char} appeared {hash_map.get(char , 0)}")