def combination_sum(candidates, target):
    res = []
    def backtrack(index,path):
        if target == sum(path):
            res.append(path.copy())
        if sum(path)> target or index > len(candidates):
            return
        for i in range(index,len(candidates)):
            path.append(candidates[i])
            backtrack(i,path)
            path.pop()
    backtrack(0,[])
    return res


candidates = [2,3,6,7]
target = 7
print(combination_sum(candidates, target))