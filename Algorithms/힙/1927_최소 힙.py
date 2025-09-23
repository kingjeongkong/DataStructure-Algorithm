import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)

"""
문제 자체에서 최소 힙을 사용하라고 함
일반 배열을 사용하게 되면 N개의 배열에서 최소값을 찾는 시간 복잡도는 O(N), 이 과정을 N번 반복해야 하므로 시간 복잡도는 O(N^2), N개의 최대값은 10만개이므로 시간 초과
최소 힙을 사용하면 시간 복잡도는 O(logN)
파이썬에서는 heapq 모듈을 사용하여 최소 힙을 구현할 수 있음
"""