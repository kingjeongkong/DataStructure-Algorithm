from collections import deque

n = int(input())
queue = deque()
for i in range(1, n+1):
    queue.append(i)

while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])

"""
단순 큐 문제
"""