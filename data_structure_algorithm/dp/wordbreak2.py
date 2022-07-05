### This will be we explained code from scratch
# First we see the recursive approach
def canConstruct_recursive(target, wordBank):
    if target == "":
        return True
    for word in wordBank:
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                if canConstruct_recursive(suffix, wordBank) == True:
                    return True
        except ValueError:
                pass
    return False



# Then we memoze the solution
def canConstruct_memoized(target, wordBank, memo = {}):
    if target in memo: return memo[target]
    if target == "":
        return True
    for word in wordBank:
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                if canConstruct_memoized(suffix, wordBank) == True:
                    memo[target]= True
                    return True
        except ValueError:
                pass
    memo[target]= False
    return False




def countConstruct_recursive(target, wordBank):
    if target == "": return 1

    global totalCount
    totalCount = 0
    for word in wordBank:
        numwaysforrest = 0
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                numwaysforrest =  countConstruct_recursive(suffix, wordBank) 
                print(numwaysforrest)
                totalCount = totalCount +numwaysforrest
        except ValueError:
                pass
    return totalCount

#print(canConstruct_memoized("abcdef",["ab","abc","cd","def","abcd"]))
#print(countConstruct_recursive("purple",["purp","p","ur","u","purpl"]))


## All COnstruct
def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    res = []
    if s in wordDict:
        res.append(s)
    for i in range(1,len(s)):
        left = s[0:i]
        if left in wordDict:
            sublist = wordBreak(s[i:],wordDict)
            for sub in sublist:
                res.append(left+" "+sub)
    return res

s = "catsanddog"
wordDict  = ["cat","cats","and","sand","dog"]
print(wordBreak(s, wordDict))


# memoized solution
def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    global memo
    memo = {}
    if s in memo:
        return memo[s]
    res = []
    if s in wordDict:
        res.append(s)
    for i in range(1,len(s)):
        left = s[0:i]
        if left in wordDict:
            sublist = wordBreak(s[i:],wordDict)
            for sub in sublist:
                res.append(left+" "+sub)
    memo[s] = res
    return res