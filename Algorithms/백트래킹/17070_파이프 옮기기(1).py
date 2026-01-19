import sys

n = int(sys.stdin.readline())
before_graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
graph = [[0]*(n+1)] + [[0] + row for row in before_graph]
answer = 0

def backtrack(y, x, shape):
    global answer
    
    if y == n and x == n:
        answer += 1
        return
    
    if shape == 'hor':
        if x+1 <= n and graph[y][x+1] == 0:
            backtrack(y, x+1, 'hor')
            
        if x+1 <= n and y+1 <= n:
            if graph[y][x+1]==0 and graph[y+1][x+1]==0 and graph[y+1][x]==0:
                backtrack(y+1, x+1, 'diag')
    elif shape == 'ver':
        if y+1 <= n and graph[y+1][x] == 0:
            backtrack(y, x+1, 'ver')
            
        if x+1 <= n and y+1 <= n:
            if graph[y][x+1]==0 and graph[y+1][x+1]==0 and graph[y+1][x]==0:
                backtrack(y+1, x+1, 'diag')
    elif shape == 'diag':
        if x+1 <= n and graph[y][x+1] == 0:
            backtrack(y, x+1, 'hor')
        
        if y+1 <= n and graph[y+1][x] == 0:
            backtrack(y, x+1, 'ver')
            
        if x+1 <= n and y+1 <= n:
            if graph[y][x+1]==0 and graph[y+1][x+1]==0 and graph[y+1][x]==0:
                backtrack(y+1, x+1, 'diag')

backtrack(1, 2, 'hor')
print(answer)


#---------------------------------------------------------------------------------

import sys

n = int(sys.stdin.readline())
before_graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
graph = [[0]*(n+1)] + [[0] + row for row in before_graph]
dp = [[[0]*3 for _ in range(n+1)] for _ in range(n+1)]

dp[1][2][0] = 1

for y in range(1, n+1):
    for x in range(1, n+1):
        if graph[y][x] == 1 or (y == 1 and x == 2):
            continue
            
        dp[y][x][0] = dp[y][x-1][0] + dp[y][x-1][2]
        dp[y][x][1] = dp[y-1][x][1] + dp[y-1][x][2]
        if graph[y-1][x] == 0 and graph[y][x-1] == 0 and graph[y][x] == 0:
            dp[y][x][2] = dp[y-1][x-1][0] + dp[y-1][x-1][1] + dp[y-1][x-1][2]

print(sum(dp[n][n]))

"""
해당 문제는 백트래킹(DFS) or DP 문제
파이프의 방향에 따라 이동, 회전이 다르므로 각각에 대해 분기처리를 해줌. 입력값이 크지 않고 N(3 ≤ N ≤ 16), 파이프가 (N, N) 위치에 도달하는 경우의 수를 모두 구해야 하므로 백트래킹(DFS)으로 접근
PyPy3으로 제출하면 통과하지만, Python3로 제출하면 시간초과.

따라서 dp로 풀기 위해 3차원 배열을 만들어줌
0 = 가로, 1 = 세로, 2 = 대각선으로 가정하고 각각에 대해 올 수 있는 경우에 대해 더해줌.
0은 이전에 가로 혹은 대각선으로 올 수 있고, 1은 이전에 세로 혹은 대각선으로 올 수 있고, 2는 이전에 가로, 세로, 대각선으로 올 수 있음. 각 경우에 맞게 방향(위치)도 같이 맞게 설정해줌
이를 이용해서 dp 배열을 채워줌.
"""