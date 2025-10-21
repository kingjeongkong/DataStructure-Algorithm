import heapq
import sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    
    if x == 0:
        if heap:
            largest = -heapq.heappop(heap)
            print(largest)
        else:
            print(0)
    elif x > 0:
        heapq.heappush(heap, -x)

"""
힙을 이용하는 문제
간단하게 힙을 사용해서 풀면 됨
힙은 최소 기능만 제공하므로 최대 힙을 사용하기 위해서는 임의로 - 부호를 붙여서 하면 됨
"""