import sys

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()
visited = [False] * n
s = []

def dfs():
    if len(s) == m:
        print(*s)
        return
    
    prev = 0
    
    for i in range(n):
        if not visited[i] and prev != num_list[i]:
            prev = num_list[i]

            s.append(num_list[i])
            visited[i] = True
            
            dfs()
            
            s.pop()
            visited[i] = False
            
dfs()