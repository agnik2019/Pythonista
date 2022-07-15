def combination_sum_2(candidates, target):
    res = []
    candidates.sort()
    def backtrack(index,path):
        if target == sum(path):
            res.append(path.copy())
        if sum(path)> target or index > len(candidates):
            return
        for i in range(index,len(candidates)):
            if i != index and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            backtrack(i,path)
            path.pop()
    backtrack(0,[])
    return res


candidates = [2,3,6,7]
target = 7
print(combination_sum_2(candidates, target))