import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
num_list = [i for i in range(1, n+1)]
for combo in combinations(num_list, m):
    print(*combo)



import sys

n, m = map(int, sys.stdin.readline().split())
s = []

def dfs(start):
    if len(s) == m:
        print(*s)
        return
    
    for i in range(start, n + 1):
        s.append(i)
        dfs(i + 1)
        s.pop()

dfs(1)

"""
해당 문제는 백트래킹 문제
처음 문제를 읽었을 때는 문제가 조합을 말하고 있어서 combinations을 사용해서 풀음.
하지만 검색해보니 이 문제의 본질은 백트래킹 알고리즘.

백트래킹은 다음과 같은 특징을 가짐
- 모든 경우를 출력해야 할 때
- 입력 크기가 작을 때
- 선택을 할 때 조건이 있을 때

그리고 백트래킹의 풀이법은 다음과 같음
1. 원하는 조건을 담을 변수를 하나 만들고
2. 조건을 만족하는 경우 처리하는 로직
3. 가능한 모두 후보를 확인하기 위한 탐색(반복문)
4. 반복문 내에서 액션(변수에 후보 담고, 재귀 함수를 호출해서 다음 단계로 넘어가고, 재귀가 끝나고 돌아오면 이전의 기록을 지움)

감이 잘 안잡히는데 좀 더 연습해봐야 할 듯
"""