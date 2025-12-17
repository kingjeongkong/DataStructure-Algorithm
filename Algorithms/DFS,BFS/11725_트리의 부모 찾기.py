import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)
parent[1] = -1
queue = deque([1])

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
while queue:
    current_node = queue.popleft()
    for next_node in graph[current_node]:
        if parent[next_node] == 0:
            parent[next_node] = current_node
            queue.append(next_node)

for i in range(2, n+1):
    print(parent[i])

"""
해당 문제는 DFS/BFS를 이용해서 해결하는 트리 문제
입력값에서 두 정점 사이의 관계가 명시적으로 나타나지 않았으므로 양방향을 모두 저장해줘야 함. -> graph라는 이중 배열 변수에 저장
노드에 개수가 10만개일수도 있으므로 DFS를 이용해서 풀면 메모리 초과가 발생할 수 있으므로 BFS로 해결
DFS/BFS를 활용하여 루트 노드인 1부터 시작해서 차례대로 탐색하여 트리를 처리함
루트 노트부터 차례대로 탐색을 시작하게 됐을 때, 현재 노드에서 특정 노드에 진입하게 되면 특정 노드의 진입점은 부모 노드에서만 진입이 가능하므로, 현재 노드를 특정 노드의 부모 노드로 설정해줌. 이를 parent라는 배열 변수에 저장해서 쉽게 부모 노드를 찾아낼 수 있도록 함
"""