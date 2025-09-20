import sys
sys.setrecursionlimit(10000)

t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    cabbage = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    answer = 0
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        cabbage[y][x] = 1

    def dfs(y, x):
        visited[y][x] = True
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < m and 0 <= ny < n:
                if cabbage[ny][nx] == 1 and visited[ny][nx] == False:
                    dfs(ny, nx)

    for y in range(n):
        for x in range(m):
            if cabbage[y][x] == 1 and visited[y][x] == False:
                answer += 1
                dfs(y, x)

    print(answer)

"""
목표 : 필요한 지렁이의 총 마리 수 구하기
규칙 : 지렁이는 상하좌우로 인접한 배추로만 이동할 수 있음
핵심 : 상하좌우로 서로 붙어있는 배추의 덩어리(그룹)이 몇개인지 세는 문제
-> 연결된 그룹 개수 세기는 DFS/BFS 문제

2차원 배열을 통해 배추밭을 만들고 배추가 있는 곳에 1을 표시 없으면 0을 표시
또 다른 2차원 배열을 통해 해당 배추를 방문했는지 표시

배추밭을 순회하면서 배추가 있고(cabbage가 1) 방문하지 않았다면(visited가 False) 지렁이 1마리 추가
그리고 해당 배추와 상하좌우로 인접해 있는 모든 배추를 방문처리하기 위해서 dfs로 처리

dfs는 먼저 dx = [0, 0, -1, 1] dy = [-1, 1, 0, 0]로 상하좌우 표시
그리고 현 위치(x,y)로부터 for문을 통해 상하좌우 값(nx, ny)를 구해서 배추 밭 내에 있는지 체크(인덱스 범위 체크)해주고 내에 있다면 배추가 있는지, 방문하지 않았는지 체크한 뒤에 또 다른 dfs를 통해 계속해서 인접 배추들을 방문처리

이 문제를 bfs로 처리한다면 큐를 하나 만들어 두고 dfs를 사용해서 재귀적으로 함수 호출하는 부분을 큐에 추가하는 방식으로 처리하면 됨.
"""