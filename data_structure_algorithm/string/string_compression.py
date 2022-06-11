def stringCompression(s):
    i,j = 0,0
    while i <len(s):
        cur = s[i]
        s[j] = cur
        i += 1
        j += 1
        cnt = 1
        while i <len(s) and cur == s[i]:
            cnt += 1
            i += 1
        if cnt > 1:
            for c in str(cnt):
                s[j] = c
                j += 1

    return j

s = ["a","a","b","b","c","c","c"]
print(stringCompression(s))