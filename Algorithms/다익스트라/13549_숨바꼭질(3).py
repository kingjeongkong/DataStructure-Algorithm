import sys
import heapq

INF = float('inf')
time_list = [INF] * 100001
n, k = map(int, sys.stdin.readline().split())
pq = []

heapq.heappush(pq, (0, n))
time_list[n] = 0

while pq:
    time, now = heapq.heappop(pq)
    
    if time_list[now] < time:
        continue
    
    if now == k:
        print(time)
        break
        
    a = now - 1
    b = now + 1
    c = now * 2
    
    if 0 <= a <= 100000 and time_list[a] > time+1:
        time_list[a] = time+1
        heapq.heappush(pq, (time+1, a))
    if 0 <= b <= 100000 and time_list[b] > time+1:
        time_list[b] = time+1
        heapq.heappush(pq, (time+1, b))
    if 0 <= c <= 100000 and time_list[c] > time:
        time_list[c] = time
        heapq.heappush(pq, (time, c))

"""
해당 문제는 숨바꼭질(BFS) 문제와 비슷하지만, 2*X의 위치로 이동하는 경우의 가중치가 0이고 나머지들은 가중치가 1로 달라서 BFS로 풀면 안되고 다익스트라로 풀어야 함.

푸는 방식은 동일함
최소 비용을 비교해줄 리스트를 무한대로 초기화해주고
우선순위 큐를 만들고 초기값을 넣어주고
반복문 내에서 우선순위 큐의 요소들을 하나씩 꺼내서 조건을 비교해서 처리해주고 time_list보다 작다면 time_list를 갱신해주고 힙큐에 추가해줌
"""