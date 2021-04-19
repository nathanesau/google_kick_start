"""
input1:
4
4
9 7 5 3
9
5 5 4 5 5 5 4 5 6
4
8 5 2 0
13
1 1 1 1 5 5 4 5 5 7 4 5 6

input2:
1
1
5

input3:
1
4
8 5 2 0
"""

# longest progression: 9pts, 12pts
def solve(t, A):
    ans = 1 if len(A) >= 1 else 0
    for i in range(0, len(A)-1):
        pv = A[i]
        pdiff = None
        adj = False
        size = 0
        for j in range(i+1, len(A)):
            v = A[j]
            diff = v - pv
            if pdiff is not None and diff != pdiff:  # adj val s.t. diff = pdiff
                if adj:  # already used
                    break
                v += (pdiff - diff)
                diff = pdiff
                adj = True
            pv = v
            pdiff = diff
            size += 1
        ans = max(ans, size+1)
    print(f"Case #{t}: {ans}")


T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    solve(t+1, A)
