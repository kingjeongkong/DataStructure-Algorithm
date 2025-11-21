import sys

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()
s = []
selected = []

def dfs():
    if len(s) == m:
        print(*s)
        return
    
    for i in range(n):
        if i in selected:
            continue
            
        s.append(num_list[i])
        selected.append(i)
        dfs()
        s.pop()
        selected.pop()

dfs()