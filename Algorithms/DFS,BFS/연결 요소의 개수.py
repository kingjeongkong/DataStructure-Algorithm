import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
count = 0

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
def bfs(start):
    visited[start] = True
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                
for node in range(1, n+1):
    if not visited[node]:
        bfs(node)
        count += 1
        
print(count)


# 연결 요소를 찾는 문제 - 방향성이 없는 그래프 문제 -> 인접 리스트로 그래프를 표현하면 됨
# 각 노드와 연결된 모든 노드를 찾고 탐색해야 하므로 DFS나 BFS가 적절함
# 모든 노드들을 for문에 넣어서 연결 요소를 찾기 - visited를 활용해서 이전의 노드에서 이미 탐색된 노드는 건너뜀

# 처음에 input()으로 입력값을 받았는데 시간 초과가 뜸 -> input = sys.stdin.readline 하는 방법에 익숙해져야겠음.