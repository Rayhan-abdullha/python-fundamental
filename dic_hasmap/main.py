from collections import defaultdict

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