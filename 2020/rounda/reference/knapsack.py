class RecursiveSolver:
    def __init__(self, w, v, N, c):
        self.w = w
        self.v = v

    def ks(self, n, c):
        if n == 0 or c == 0:
            result = 0
        elif self.w[n] > c:  # exclude item n
            result = self.ks(n-1, c)
        else:
            tmp1 = self.ks(n-1, c)
            tmp2 = self.v[n] + self.ks(n-1, c-w[n])
            result = max(tmp1, tmp2)
        return result


class DPSolver:
    def __init__(self, w, v, N, c):
        self.w = w
        self.v = v
        self.dp = [[None for j in range(c+1)] for i in range(N+1)] # N*c

    def ks(self, n, c):        
        if self.dp[n][c] != None:
            return self.dp[n][c]
        if n == 0 or c == 0:
            result = 0
        elif w[n] > c:
            result = self.ks(n-1, c)
        else:
            tmp1 = self.ks(n-1, c)
            tmp2 = self.v[n] + self.ks(n-1, c-w[n])
            result = max(tmp1, tmp2)
        self.dp[n][c] = result
        return result


# knapsack problem (non-DP)
N = 5
w = [None,1,2,4,2,5]
v = [None,5,3,5,3,2]
c = 10

s1 = RecursiveSolver(w, v, N, c)
print(s1.ks(N, c))

s2 = DPSolver(w, v, N, c)
print(s2.ks(N, c))
