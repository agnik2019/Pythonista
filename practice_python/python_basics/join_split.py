data = "this is data"
d = " "
print(data.split(d))

data2 = ['this', 'is', 'data']
print("".join(data))

data3 = ['this', 'is', 'data',5,10]
print(" ".join(str(i) for i in data3)) #generator expression
