import sys
import heapq

INF = float('inf')
V, E = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
pq = [(0, k)]
dist_list = [INF] * (V+1)
dist_list[k] = 0

while pq:
    dist, now = heapq.heappop(pq)
    
    if dist_list[now] < dist:
        continue
        
    for next_node, weight in graph[now]:
        cost = dist + weight
        if dist_list[next_node] > cost:
            dist_list[next_node] = cost
            heapq.heappush(pq, (cost, next_node))

for i in dist_list[1:]:
    if i >= INF:
        print("INF")
    else:
        print(i)

"""
일반적인 다익스트라 알고리즘 문제

주의점 : 힙큐는 앞의 값부터 비교하므로 거리가 제일 앞에 와야 함. 
graph 배열에 저장되는 순서랑 맞춰보겠다고 힙큐의 순서도 바꾸면 안됨...
"""