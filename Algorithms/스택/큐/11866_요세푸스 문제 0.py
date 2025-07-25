from collections import deque

n, k = map(int, input().split())
queue = deque()
for i in range(1, n+1):
    queue.append(i)
answer = []

while True:
    if len(queue) == 1:
        answer.append(queue.pop())
        break
    
    for _ in range(k-1):
        m = queue.popleft()
        queue.append(m)
        
    answer.append(queue.popleft())

print(f"<{', '.join(map(str, answer))}>")

"""
이 문제는 큐를 이용해서 풀이 가능한 문제

K번째 사람을 줄에서 제거한 후, 다음 사람을 제거할 때 이전의 제거된 인덱스부터 시작함.
따라서 큐를 사용하여 줄을 만들어 k-1명의 사람을 popleft로 제거한 후 append하여 줄을 이어줌.
-> 이전에 제거된 사람의 인덱스부터 k번째의 사람을 쉽게 찾아낼 수 있음.
"""