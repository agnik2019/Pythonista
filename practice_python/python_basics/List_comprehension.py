###list comprehension
l1 = [ x**2 for x in range(6,0,-1)]
print(l1)

####set
# given_list = [1,2,1,2,3,4,6,3]
# #print the sum of given list of unique elements
# new_set = set()
# for x in given_list:
#     new_set.add(x)
# total = 0
# for x in new_set:
#     total += x
# print(total)

list1 = [1,2,3,5,4,33,24,45,43,233,33]
divide_by_3 = []
for no in list1:
    if no%3 == 0:
        divide_by_3.append(no)
print("without using list comprehension ",divide_by_3)
print("Using List comprehension",[item for item in list1 if item%3==0])

# dictionary comprehention
dict1 = {'a': 45, 'b':65, 'A':5}
print({k.lower(): dict1.get(k.lower(),0)+dict1.get(k.upper(),0) for k in dict1.keys()})


## set comprehension
