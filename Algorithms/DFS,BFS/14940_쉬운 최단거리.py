import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
map_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
move_list = [(0, -1), (0, 1), (-1, 0), (1, 0)]
answer = [[-1] * m for _ in range(n)]
targetY = 0
targetX = 0

def bfs(y, x):
    queue = deque([(y, x, 0)])
    visited[y][x] = True
    answer[y][x] = 0
    
    while queue:
        cur_y, cur_x, move_num = queue.popleft()
        
        for move in move_list:
            dx, dy = move
            nx = dx + cur_x
            ny = dy + cur_y
            
            if 0 <= ny < n and 0 <= nx < m:
                if map_list[ny][nx] == 1 and visited[ny][nx] == False:
                    answer[ny][nx] = move_num + 1
                    visited[ny][nx] = True
                    queue.append((ny, nx, move_num + 1))
        

for y in range(n):
    for x in range(m):
        if map_list[y][x] == 2:
            targetY = y
            targetX = x
        elif map_list[y][x] == 0:
            answer[y][x] = 0

bfs(targetY, targetX)
            
for row in answer:
    for i in row:
        print(i, end=" ")
    print()


"""
각 모든 지점에서 목표지점까지의 최단거리를 구하는 문제 -> 최단거리를 구하는 문제이므로 bfs를 떠올릴 수 있음.

초기 접근법은 bfs 함수를 만들어서 각 모든 지점에 대해서 bfs를 실행하고 각 지점에서의 최단거리를 매번 구하려고 했음.
이를 위해서는 visited도 매번 초기화해서 생성해주어야 했음.
-> 이 방식으로는 visited를 매번 초기화해서 생성해주어야 하므로 메모리 초과가 발생, 그리고 지도의 모든 지점에 대해서 bfs를 실행하므로 시간 초과도 발생

따라서 반대로 접근함. 목표지점에서부터 각 모든 지점까지의 최단 거리를 구하는 방식 -> bfs를 한번만 하면 됨
1인 지점을 탐색하고 2인 지점이나 0인 지점은 0으로 초기화, 갈 수 없는 지점은 -1로 초기화
따라서 bfs 안에서는 1인 지점만 탐색해주고, 함수 밖에서 answer는 기본적으로 -1로 전체 초기화를 해주고 map_list에서 2, 0 인 지점의 answer는 0으로 초기화
"""