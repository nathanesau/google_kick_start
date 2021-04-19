# allocation: 5pts, 7pts
def solve(t, n, money, cost):
    index = -1
    while money >= 0 and index < len(cost) - 1:
        money -= cost[index+1]
        if money >= 0:
            index += 1
    ans = index+1
    print(f"Case #{t}: {ans}")

"""
T = int(input())
for t in range(T):
    n, money = map(int, input().split())
    cost = sorted(list(map(int, input().split())))
    solve(t+1, n, money, cost)
"""

solve(t=1, n=4, money=100, cost=[20,40,90,90])
solve(t=2, n=4, money=50, cost=[10,10,30,30])
solve(t=3, n=3, money=300, cost=[999,999,999])