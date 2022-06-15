import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        def isNotVisited(x, path):
            size = len(path)
            for i in range(size):
                if (path[i] == x):
                    return 0              
            return 1
        queue = collections.deque()
        vis = set()
        words = set(wordList)
        allpaths = []
        path = []
        level,minlevel = 0,1e7
        if endWord not in words:
            return allpaths
        path.append(beginWord)
        vis.add(beginWord)
        queue.append(path[:])
        while queue:
            levelsize = len(queue)
            level += 1
            for i in range(levelsize):
                path = queue.popleft()
                last = path[len(path) - 1]
                if last == endWord:
                    minlevel = min(minlevel,level)
                    if len(path) > minlevel:
                        break
                    allpaths.append(path)
                    continue
                for j in range(len(last)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        t = last[:j] + c + last[j+1:]
                        if t in words and t not in vis:
                            newpath = path[:]
                            newpath.append(t)
                            vis.add(t)
                            queue.append(newpath)
                            vis.remove(t)
        return allpaths
        

# beginWord = "qa"
# endWord = "sq"
# wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln",
#             "tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo",
#             "ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc"
#             ,"lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li"
#             ,"ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st"
#             ,"er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
beginWord,endWord = "hit","cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().findLadders(beginWord, endWord, wordList))