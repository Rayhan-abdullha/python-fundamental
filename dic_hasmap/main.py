from collections import defaultdict
# HashMap (aka dict)
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
print(len(myMap))

myMap["alice"] = 80
print(myMap["alice"])

print("alice" in myMap)
myMap.pop("alice")
print("alice" in myMap)

myMap = { "alice": 90, "bob": 70 }
print(myMap)

# Dict comprehension
myMap = { i: 2*i for i in range(3) }
print(myMap)

# Looping through maps
myMap = { "alice": 90, "bob": 70 }
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)


person = {
    "name": 'coder',
    "age": 25,
    "grades": {"bangla": 33},
    "10": [10, 100]
}
# print(person)

# hasing
nums = [1,2,3,4,5,6,7]
dic = defaultdict(list)
for num in nums:
    dic[num%2].append(num)
print(dic) 


# dic looping
for key, val in person.items():
    print(key,  "value: ", val)