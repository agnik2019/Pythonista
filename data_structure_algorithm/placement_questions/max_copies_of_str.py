import collections


str1 = "BILLOBILLOLLOBBI"
str2 = "BILL"

mp1 = collections.Counter(str1)
mp2 = collections.Counter(str2)

mn = float("inf")
for x,y in mp2.items():
    mn = min(mn, mp1[x]//y)
print(mn)