import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
tomato_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
move_list = [(0, -1), (0, 1), (-1, 0), (1, 0)]
queue = deque()
answer = 0
complete = True

def bfs():
    global answer
    
    while queue:
        y, x, day = queue.popleft()
        if answer < day:
            answer = day
        
        for move in move_list:
            dx, dy = move
            nx = dx + x
            ny = dy + y
            
            if 0 <= nx < m and 0 <= ny < n:
                if tomato_list[ny][nx] == 0:
                    tomato_list[ny][nx] = 1
                    queue.append((ny, nx, day + 1))
                    
for y in range(n):
    for x in range(m):
        if tomato_list[y][x] == 1:
            queue.append((y, x, 0))
            
bfs()

for y in range(n):
    for x in range(m):
        if tomato_list[y][x] == 0:
            complete = False
            break

if complete:
    print(answer)
else:
    print(-1)

"""
해당 문제는 토마토가 익는 최소 일수를 구하는 문제
인접한 토마토, 최소 일수라는 키워드를 보면 BFS를 떠올릴 수 있음

인접한 토마토가 1일이 지나면 익은 토마토가 되므로 큐에 인접한 토마토를 추가할 때 1일을 더해서 추가해주면 됨
토마토를 방문하고 나면 익은 토마토가 돼서 1이 되므로 visited가 필요없고 토마토 위치가 0인지 1인지 체크해주면 방문 체크도 가능
1인 토마토(익은 토마토)가 처음에 여러 개일수도 있으므로, 반복문을 통해 모든 위치를 탐색해서 1인 토마토를 모두 큐에 추가해서 한꺼번에 처리해줌.
이후 토마토 리스트에서 -1(비어있는 자리)때문에 방문할 수가 없어 0인 토마토가 남아있으면 모두 익지 못하는 상황이므로 -1 출력
"""