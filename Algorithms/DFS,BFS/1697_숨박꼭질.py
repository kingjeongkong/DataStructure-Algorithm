import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque([(n, 0)])
visited = [0] * 100001
visited[n] = 1

def solve():
    if n == k:
        print(0)
        return

    while queue:
        position, time = queue.popleft()
            
        a = position + 1
        b = position - 1
        c = position * 2
        if a == k or b == k or c == k:
            print(time + 1)
            return
        
        if 0 <= a <= 100000 and visited[a] == 0:
            queue.append((a, time + 1))
            visited[a] = 1
        if 0 <= b <= 100000 and visited[b] == 0:
            queue.append((b, time + 1))
            visited[b] = 1
        if 0 <= c <= 100000 and visited[c] == 0:
            queue.append((c, time + 1))
            visited[c] = 1

solve()

#---------------------------------------------------------
def solve():
    if n == k:
        print(0)
        return

    while queue:
        position, time = queue.popleft()

        if position == k:
            print(time)
            return
        
        for next_pos in [position - 1, position + 1, position * 2]:
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = 1
                queue.append((next_pos, time + 1))

#--------------------------------------------------------
def solve():
    if n == k:
      print(0)
      return

    while queue:
      position, time = queue.popleft()

      next_positions = [position - 1, position + 1, position * 2]

      for next_pos in next_positions:
          if next_pos == k:
              print(time + 1)
              return

          if 0 <= next_pos <= 100000 and not visited[next_pos]:
              visited[next_pos] = 1
              queue.append((next_pos, time + 1))

"""
해당 문제는 모든 행동의 가중치가 1인 경우에 대해서 최소 시간을 구하는 문제이므로 BFS을 활용해서 풀어야 함
BFS 문제를 풀기 위해서는 큐와 방문 처리(이미 방문한 곳 중복 방문 방지)를 해줘야 함.
큐와 visited를 초기화 해준 후
bfs의 기본 구조인 while 반복문에서 큐가 빌 때까지 반복해주고
반복문 내에서 큐의 값을 앞에서 하나 꺼내 원하는 작업을 처리해줌
이 문제는 +1, -1, *2의 경우에 대해서 처리하고 k와 같은지 비교. -> 만약 다르다면 해당 위치의 범위 체크 및 방문 여부 체크 후 큐에 추가
만약 같다면 그때의 시간을 출력하고 함수 종료
"""