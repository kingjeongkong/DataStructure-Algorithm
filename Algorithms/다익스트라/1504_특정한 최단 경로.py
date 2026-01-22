import sys
import heapq

INF = float('inf')
n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(start):
    dist_list = [INF] * (n+1)
    pq = []
    dist_list[start] = 0
    heapq.heappush(pq, (0, start))
    
    while pq:
        dist, now = heapq.heappop(pq)
        
        if dist_list[now] < dist:
            continue
            
        for next_node, weight in graph[now]:
            cost = dist + weight
            if dist_list[next_node] > cost:
                heapq.heappush(pq, (cost, next_node))
                dist_list[next_node] = cost
                
    return dist_list

dist_1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

path1 = dist_1[v1] + dist_v1[v2] + dist_v2[n]
path2 = dist_1[v2] + dist_v2[v1] + dist_v1[n]
answer = min(path1, path2)
if answer >= INF:
    print(-1)
else:
    print(answer)


"""
해당 문제는 1번 정점에서 N번 정점으로 최단 거리를 구하는 다익스트라 문제
1916_최소 비용 구하기 문제와 비슷하지만 중간에 거쳐가야 하는 경유지가 있음.
경유지가 있을 경우 출발지부터 경유지까지 최단 거리를 구하고(다익스트라) 경유지로부터 다시 도착지까지 최단 거리를 구하면 됨.
이 문제는 경유지가 총 2개이므로 출발지에서 경유지1, 경유지1에서 경유지2, 경유지2에서 도착지까지 최단 거리를 구하면 됨.
총 3번의 다익스트라 알고리즘을 활용해서 풀어야 함.
"""