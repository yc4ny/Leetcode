class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u = 0
        d = 0 
        l = 0 
        r = 0 
        for move in moves:
            if move == "U":
                u += 1
                continue
            if move == "D":
                d += 1
                continue
            if move == "L":
                l += 1
                continue
            if move == "R":
                r += 1
        if u == d and l == r:
            return True
        else:
            return False