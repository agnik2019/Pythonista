x = [[-1,2],[3,4],[5,6],[-5,10],[12,3]]
# x.sort()
# print(x)

# x.sort(reverse=True)
# print(x)

# x.sort(key = lambda x : x[1])
# print(x)

x.sort(key = lambda x : x[1]+x[0])
print(x)