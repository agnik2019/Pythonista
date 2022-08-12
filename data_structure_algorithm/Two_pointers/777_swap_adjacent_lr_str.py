class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace("X","") != end.replace("X",""):
            return False
        startL = [i for i in range(len(start)) if start[i] == 'L']
        endL = [i for i in range(len(end)) if end[i] == 'L']
        
        startR = [i for i in range(len(start)) if start[i] == 'R']
        endR = [i for i in range(len(end)) if end[i] == 'R']
        
        for i,j in zip(startL,endL):
            if i<j:
                return False
        
        for i,j in zip(startR,endR):
            if i>j:
                return False
        return True