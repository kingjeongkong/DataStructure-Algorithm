import sys

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()
selected = []

def dfs(cur):
    if len(selected) == m:
        print(*selected)
        return
    
    prev = 0
    
    for i in range(n):
        if prev != num_list[i] and cur <= num_list[i]:
            prev = num_list[i]
            
            selected.append(num_list[i])
            dfs(num_list[i])
            selected.pop()

dfs(0)

"""
N과 M(9)번 문제와 유사.
다른 점은 사용한 수를 재사용할 수 있다는 것과, 수열이 오름차순이어야 한다는 것.
N과 M(9)번 문제처럼 중복되는 수열은 안되므로 prev 변수를 사용해서 수열이 중복되지 않게 함.
하지만 수를 재사용할 수 있으므로 visited 변수는 필요하지 않음
그리고 오름차순을 처리해주기 위해 dfs 함수에 파라미터로 cur을 받아 이전에 선택한 수보다 큰 지 확인해줌
"""