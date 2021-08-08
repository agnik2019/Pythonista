# For ELse & While Else

search = [1,2,3,4,5,6,7,8]
target = 10
for element in search:
    if element == target:
        print("I Found it")
        break
else:
    print("I didn't find it")



i = 0
while i < len(search):
    element = search[i]
    if element == target:
        print("I Found it")
        break
    i += 1
else:
    print("I didn't find it")