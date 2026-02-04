import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    queue = deque([(a, '')])
    visited = [False] * 10000
    
    while queue:
        now, comm = queue.popleft()
        
        if now == b:
            print(''.join(comm))
            break
            
        D = 2 * now % 10000
        S = 9999 if now == 0 else now - 1
        L = ((now % 1000) * 10) + (now // 1000)
        R = ((now % 10) * 1000) + (now // 10)
            
        if visited[D] == False:
            visited[D] = True
            queue.append((D, comm + 'D'))
        if visited[S] == False:
            visited[S] = True
            queue.append((S, comm + 'S'))
        if visited[L] == False:
            visited[L] = True
            queue.append((L, comm + 'L'))
        if visited[R] == False:
            visited[R] = True
            queue.append((R, comm + 'R'))

"""
A에서 B로 변환하기 위해 필요한 최소한의 명령어(명령어는 총 4가지)의 나열 -> BFS 문제
일반적인 BFS 문제처럼 queue, visited 배열을 초기화 해주고 
while queue:에서 큐에 현재 값이랑 명령어를 튜플로 저장해주고 각 4가지 명령어에 대해 연산을 한 뒤 방문 여부를 체크하고 큐에 넣어주면 됨.
while 문의 초기에 현재 값이 B와 같은지 확인해주면서 같다면 명령어 출력하고 종료
"""