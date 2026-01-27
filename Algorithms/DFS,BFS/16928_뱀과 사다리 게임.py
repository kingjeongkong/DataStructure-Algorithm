import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
move = [0] * 101
for _ in range(n+m):
    x, y = map(int, sys.stdin.readline().split())
    move[x] = y

queue = deque([(1, 0)])
visited = [False] * 101
visited[1] = True

while queue:
    now, num = queue.popleft()
    
    if now == 100:
        print(num)
        break
        
    for i in range(1, 7):
        next_node = i + now
        
        if next_node <= 100:
            if move[next_node] != 0:
                next_node = move[next_node]
            
            if visited[next_node] == False:
                visited[next_node] = True
                queue.append((next_node, num+1))

"""
해당 문제는 100에 도착하는 주사위 횟수의 최솟값을 구하는 문제
여러 가지 상황 중에서 최솟값을 구해야 하므로 BFS 문제

처음에는 사다리, 뱀 케이스를 각각 저장하고 큐에 1부터 시작해 주사외 1~6의 숫자를 반복문으로 각각 더한 후 각 숫자들이 사다리나 뱀의 케이스에 있는지 확인하고 있으면 이동하는 숫자를 큐에 넣어줌. 이후 while문을 돌리면서 100에 도달하는 순간을 찾음

다른 방법으로는 사다리, 뱀 모두 한꺼번에 입력값으로 받아 1-100까지의 move 배열의 각 인덱스들의 배열값으로 이동하는 숫자를 저장해줌. 이동하지 않으면 0 그대로 두고. 이후 while 문에서 내에서 아까와 같이 1~6의 숫자를 반복문으로 각각 더한 후 범위 체크 후 move 배열해서 각 숫자들에 대하여 사다리나 뱀으로 이동하는지 확인 후 큐에 추가하고 처리해줌.
"""