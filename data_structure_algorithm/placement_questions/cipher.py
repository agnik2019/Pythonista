s = str(input())
mp = {}
val = "A"
for c in s:
    if c not in mp:
        mp[c] = val
        val = chr(ord(val)+1)
res = ""
for c in s:
    res += mp[c]
print(res)

