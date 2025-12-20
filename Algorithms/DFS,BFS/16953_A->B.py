import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
queue = deque([(a, 0)])

def bfs():
    while queue:
        cur_num, times = queue.popleft()
        if cur_num == b:
            return times+1
        
        if cur_num*2 <= b:
            queue.append((cur_num * 2, times + 1))
        if int(str(cur_num)+'1') <= b:
            queue.append((int(str(cur_num)+'1'), times + 1))
    else:
        return -1

print(bfs())

"""
해당 문제는 '2를 곱하거나, 1을 수의 가장 오른쪽에 추가해서' A를 B로 만드는데 문제
1697(숨박꼭질) 문제와 비슷해서 bfs로 풀어야 한다는걸 캐치
이외에도 최소값을 찾아야 하며, 상태가 가지치기 처럼 뻗어나감(트리 형태) -> BFS 문제
따라서 bfs로 풀어줌. 
-> queue를 활용하여 현재 수와 연산 횟수를 튜플로 큐에 저장. 
-> 현재 수가 b보다 작거나 같을 때면 큐에 추가해줌
"""