import sys
import heapq

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    max_q = []
    min_q = []
    deleted_q = {}
    
    for _ in range(k):
        operation, num = sys.stdin.readline().strip().split()
        n = int(num)
        if operation == 'I':
            heapq.heappush(max_q, -n)
            heapq.heappush(min_q, n)
            deleted_q[n] = deleted_q.get(n, 0) + 1
        else:
            if n == 1 and max_q:
                while max_q and deleted_q.get(-max_q[0], 0) == 0:
                    heapq.heappop(max_q)
                if max_q:
                    largest = -heapq.heappop(max_q)
                    deleted_q[largest] -= 1
                    if deleted_q[largest] == 0:
                        del deleted_q[largest]
            elif n == -1 and min_q:
                while min_q and deleted_q.get(min_q[0], 0) == 0:
                    heapq.heappop(min_q)
                if min_q:
                    smallest = heapq.heappop(min_q)
                    deleted_q[smallest] -= 1
                    if deleted_q[smallest] == 0:
                        del deleted_q[smallest]
                        
    while max_q and deleted_q.get(-max_q[0], 0) == 0:
        heapq.heappop(max_q)
    while min_q and deleted_q.get(min_q[0], 0) == 0:
        heapq.heappop(min_q)
                    
    if max_q and min_q:
        print(-max_q[0], min_q[0])
    else:
        print("EMPTY")

"""
해당 문제는 힙을 사용하는 이중 우선순위 큐 문제
문제 제목부터 이중 우선순위 큐이므로 두개의 우선순위 큐를 사용해서 각각 최대 큐, 최소 큐를 만듦
각 큐에 숫자를 삽입하는건 문제 없지만 삭제에서 최대값, 최소값 삭제를 구분해야 함. 이 부분에서 각각 최대 큐, 최소 큐를 사용하면 되지만 한쪽에서 삭제하면 다른 큐도 같이 동기화를 해줘야 함. 만약 다른쪽 큐에서 직접 값을 찾아서(그 큐 내에서 최대, 최소가 아닌 값) pop을 하려고 하면 O(N)이므로 전체 시간복잡도는 O(N^2)이므로 시간초과 발생.
따라서 각 최대, 최소 값에 따라 맞는 큐에서 heappop을 해주고 나머지 큐는 당장 제거해주는 것이 아닌 해당 값이 삭제됐다는 여부만 체크하고 나중에 heappop을 할 때 한꺼번에 처리하는 방식으로 해야 함.
삭제 여부 체크는 딕셔너리를 사용해 빠르게 접근 가능하게 구현

결국 이 문제의 핵심 관건은 동기화임.
한쪽 큐에서는 최소 or 최대에 대해 heappop으로 쉽게 제거가 가능한데 다른 큐에서 그 값은 중간에 껴있는 값일 가능성이 크므로 직접 찾아서 pop을 해주는게 아닌, 해당 값이 삭제 됐다는 여부만 체크하고 추후 해당 큐에서 heappop을 해야 할 때 맨 위 값의 삭제 여부를 체크하면서 제거를 진행해 나감. 왜냐하면 이 큐의 관심사는 맨 위의 값이지 중간의 값이 아님. 중간에 죽은 값이 껴있어도 맨 위로 올라오지 않는 이상 상관없음 
"""