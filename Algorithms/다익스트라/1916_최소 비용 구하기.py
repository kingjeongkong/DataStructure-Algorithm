import sys
import heapq

INF = float('inf')
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    n1, n2, weight = map(int, sys.stdin.readline().split())
    graph[n1].append((n2, weight))
start, end = map(int, sys.stdin.readline().split())
distance = [INF] * (n+1)
pq = []

heapq.heappush(pq, (0, start))
distance[start] = 0

while pq:
    dist, now = heapq.heappop(pq)
    
    if distance[now] < dist:
        continue
        
    for next_node, weight in graph[now]:
        cost = dist + weight
        if distance[next_node] > cost:
            distance[next_node] = cost
            heapq.heappush(pq, (cost, next_node))

print(distance[end])


"""
해당 문제는 출발점에서 도착점까지 도달하는데 최소 비용을 구하는 문제
각 경로별로 가중치가 있으므로, BFS로 풀면 안되고 다익스트라 알고리즘을 이용해서 풀어야 함.

우선 중복 경로 방지와 최단 거리 값이 들어갈 distance 배열을 무한대로 초기화해줌.
graph 배열에 각 노드와 가중치를 저장해줌.
그리고 다익스트라는 우선순위 큐를 활용해서 풀어야 하므로 힙큐를 하나 만들어줌.

이후 힙큐 안의 모든 요소를 다 처리할 때까지 반복문을 돌려주는데
반복문 내에서는 힙큐의 최소값을 하나씩 꺼내서 처리해줌
-> pop한 노드까지의 거리가 distance 배열에 저장된 값보다 크다면 이미 최소 거리는 처리된거므로 continue로 넘어가줌
-> 아니라면 해당 노드와 연결된 모든 노드에 대해서 거리를 계산해서 마찬가지로 distance보다 작다면 distance 배열을 갱신해주고 힙큐에 추가해줌
"""