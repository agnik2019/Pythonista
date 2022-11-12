# Write a program to generate a simple pattern.
# 1
# 12
# 123
# 1234
# 123
# 12
# 1
n = 4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")
for i in range(n,0,-1):
    for j in range(1,i):
        print(j,end="")
    print("")