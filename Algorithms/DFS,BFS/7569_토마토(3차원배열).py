import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
tomato_list = []
move_list = [(0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0), (0, 0, 1), (0, 0, -1)]
queue = deque()
answer = 0
for _ in range(h):
    floor = []
    for _ in range(n):
        floor.append(list(map(int, sys.stdin.readline().split())))
    tomato_list.append(floor)

def bfs():
    global answer
    
    while queue:
        z, y, x, time = queue.popleft()
        answer = time
        
        for move in move_list:
            dx, dy, dz = move
            nx = dx + x
            ny = dy + y
            nz = dz + z
            
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if tomato_list[nz][ny][nx] == 0:
                    tomato_list[nz][ny][nx] = 1
                    queue.append((nz, ny, nx, time + 1))

for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomato_list[z][y][x] == 1:
                queue.append((z, y, x, 0))

bfs()

for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomato_list[z][y][x] == 0:
                print(-1)
                sys.exit(0)
else:
    print(answer)

"""
해당 문제는 이전 토마토 문제와 동일.
다른 점은 토마토가 2차원 배열에서 3차원 배열로 주어지고 상하좌우에서 더 추가로 위, 아래 방향으로 이동할 수 있도록 추가해줘야 함.
따라서 move_list에 x,y,z 좌표로 위 아래 방향도 추가해줌
입력값을 받을 때도 3차원 배열로 받아줌
이외의 로직은 z값을 비교해주는 로직을 추가해주면 됨
"""