"""
input:
2
7 5
2 1 2 4
2 3 7 8
3 4 6 2
5 3 9 9
2 6 1 5
7 1 5 7
5 10
5 8
4 1
6 1
7 6
3 2
1 2 2 10
3 2 3 5
3 2
3 3
"""
# truck: 13pts, 24pts
from functools import reduce
def gcd(a,b):
    if a==0:
        return b 
    else:
        return gcd(b%a,a)

def gcd_list(A):
    gcdp = reduce(lambda x,y:gcd(x,y),A)
    return gcdp

def bfs(graph, src, dest):
    parent = {src: None}
    visited = set([src])
    q = [src]
    while q:
        node = q.pop(0)
        if node == dest:
            path = []
            curr = dest
            while curr != None:
                path.insert(0, curr)
                curr = parent[curr]
            return path
        for neighbor in graph[node]:
            city, limit, charge = neighbor["city"], neighbor["limit"], neighbor["charge"]
            if city not in visited:
                visited.add(city)
                parent[city] = node
                q.append(city)
T = int(input())
for t in range(T):
    N, Q = map(int, input().split())
    graph = dict((k+1,[]) for k in range(N))
    data = []
    for n in range(N-1):
        X, Y, L, A = map(int, input().split())
        graph[X].append({"city": Y, "limit": L, "charge": A})
        graph[Y].append({"city": X, "limit": L, "charge": A})
    ans = []
    for q in range(Q):
        C, W = map(int, input().split())
        path = bfs(graph, C, 1)
        charges = []
        for i in range(len(path)-1):
            city1 = path[i]
            city2 = path[i+1]
            for item in graph[city1]:
                if item['city'] == city2:
                    limit = item['limit']
                    charge = item['charge']
                    if W >= limit:
                        charges.append(charge)
                    break
        if charges:
            ans.append(gcd_list(charges))
        else:
            ans.append(0)
    res = ' '.join(map(str, ans))
    print(f"Case #{t+1}: {res}")
