"""
input:
2
4
ABBC
6
ABACDA
"""

# substring: 5pts, 7pts
def solve(t, S):
    ans = []
    for i in range(len(S)):
        out = S[0]
        #for j in range(1,i+1):
        for j in range(i, 0, -1):
            if S[j-1] < S[j]:
                out += S[j]
            else:
                break
        ans.append(len(out))
    print(f"Case #{t}: {' '.join(map(str, ans))}")

T = int(input())
for t in range(T):
    N = int(input())
    S = input()
    solve(t+1, S)
