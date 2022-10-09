class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = []
        n = len(tiles)
        print(1<<3)
        for num in range(1<<n):
            s = ""
            for i in range(n):
                if num & (1<<i):
                    s += tiles[i]
            if len(s)>0: res.append(s)
        print(res)