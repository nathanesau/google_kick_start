"""
input:
2
2 4 5
10 10 100 30
80 50 10 50
3 2 3
80 80
15 50
20 10
"""
import copy


class Solver:
    def __init__(self, v, N, K, P):
        self.v = v
        self.N = N
        self.K = K
        self.P = P
        self.dp = [[0 for _ in range(P+1)] for _ in range(N+1)] # N*P

    def ks(self, i, c):  # ith stack
        if i >= self.N or c <= 0:
            return 0
        if self.dp[i][c] != None:
            return self.dp[i][c]
        result = 0
        for j in range(0, min(c, self.K) + 1):
            tmp = self.ks(self, i+1, c-j)
            if j > 0:
                tmp += self.v[i][j-1]
            result = max(result, tmp)
        self.dp[i][c] = result
        return result


T = int(input())
for t in range(T):
    N, K, P = map(int, input().split())
    """
    N: num_stacks
    K: plates_per_stack
    P: capacity
    """
    v = []
    for n in range(N):
        v.append(list(map(int, input().split())))
    """
    NOTE: weights = values
    """
    s = Solver(v, N, K, P) 
    print(s.ks(0, P))
