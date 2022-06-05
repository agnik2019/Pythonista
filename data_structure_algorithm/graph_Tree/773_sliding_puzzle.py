def slidingPuzzle( board):
    """
    :type board: List[List[int]]
    :rtype: int
    """
    begin = ''.join(str(d) for row in board for d in row)
    end = "123450"
    moves = [[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]
    queue = []
    seen = set()
    queue.append((begin,0))
    seen.add(begin)
    while queue:
        cur,level = queue.pop(0)
        if cur == end:
            return level
        idx = cur.index('0')
        for i in moves[idx]:
            new_state = list(cur)
            new_state[idx],new_state[i] = new_state[i], new_state[idx]
            new_state = "".join(new_state)
            if new_state not in seen:
                queue.append((new_state,level+1))
                seen.add(new_state)
    return -1


board = [[4,1,2],[5,0,3]]
print(slidingPuzzle(board))