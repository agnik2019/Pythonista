def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    queue = []
    vis = set()
    words = set(wordList)
    queue.append(beginWord)
    vis.add(beginWord)
    res = 0
    while queue:
        levelsize = len(queue)
        res += 1
        for i in range(levelsize):
            s = queue.pop(0)
            if s == endWord:
                return res
            for j in range(len(s)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    t = s[:j] + c + s[j+1:]
                    if t in words and t not in vis:
                        queue.append(t)
                        vis.add(t)
    return 0
                        
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord, endWord, wordList))