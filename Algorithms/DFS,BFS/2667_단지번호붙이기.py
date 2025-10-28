import sys

n = int(sys.stdin.readline())
house = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
move_list = [(0, -1), (0, 1), (-1, 0), (1, 0)]
answer = []
near_house_num = 0

def dfs(y, x):
    global near_house_num
    visited[y][x] = True
    near_house_num += 1
    
    for move in move_list:
        dx, dy = move
        nx = x + dx
        ny = y + dy
        
        if 0 <= nx < n and 0 <= ny < n:
            if house[ny][nx] == 1 and visited[ny][nx] == False:
                dfs(ny, nx)

for y in range(n):
    for x in range(n):
        if house[y][x] == 1 and visited[y][x] == False:
            dfs(y, x)
            answer.append(near_house_num)
            near_house_num = 0

print(len(answer))
for i in sorted(answer):
    print(i)

"""
해당 문제는 유기농 배추와 거의 똑같은 dfs 문제

2차원 지도에서 연결된 덩어리들을 찾아야 하는 문제이므로 바로 dfs를 떠올릴 수 있음
dfs로 풀기 위해서는 2차원 지도, visited, move(dx, dy)를 먼저 선언해줘야 함
이후 dfs 함수 내에서 먼저 visited를 체크해준 후 상하좌우 이동 방향에 대해 반복문을 통해 nx, ny가 범위 내에 있는지 다음 위치에 해당 값이 있는지 visited를 했는지 체크해준 후 dfs 실행.

이후 dfs 함수를 가지고 2차원 지도를 순회하면서 조건에 맞으면 dfs 실행. 이후의 정답값 처리는 문제에 따라서 해줌.
이 문제에서는 단지(그룹) 내 집의 개수를 찾아야 하므로 dfs 내에서 집의 개수를 +해서 구해준 후 정답 리스트에 추가해준 후 초기화.
"""