import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))

"""
해당 문제는 힙을 이용하는 문제
문제의 조건은 절대값이 가장 작은 값을 출력하고, 만약 절대값이 같으면 실제 값이 가장 작은 수를 출력해야 한다
따라서 비교를 2번 해야 함.
힙은 앞에 있는 값들을 먼저 기준으로 비교하고, 이후에 뒤에 있는 값들을 기준으로 비교함. -> 따라서 튜플 형태로 절대값을 먼저 넣고 그 뒤에 실제 값을 넣게 해서 비교할 수 있게 해줌
"""