import sys

n, m = map(int, sys.stdin.readline().split())
tree_list = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(tree_list)
answer = 0

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for tree in tree_list:
        if tree - mid > 0:
            sum += tree - mid
    
    if sum >= m:
        answer = mid
        start = mid + 1
    elif sum < m:
        end = mid - 1

print(answer)

"""
해당 문제는 M미터 이상의 나무를 가져가기 위한 절단기의 최대 높이를 구하는 문제
초기 접근법: 절단기의 높이를 가장 큰 나무의 높이부터 설정해 1씩 줄여나가면서 M미터 이상의 나무를 가져가는지 확인 -> 입력값이 (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)이므로 시간 초과

따라서 최적의 값(최대/최소)를 찾기 위해서 이진 탐색으로 풀어야 함(입력값이 크기에 범위로 줄여나감 -> O(NlogN))
딱 떨어지는 M를 구하는 것이 아닌 최소 M미터 이상의 나무를 가져가는 것이기에 꼭 sum == m 이 아니어도 정답이 될 수 있음. 따라서 sum >= m 일시 answer에 mid를 넣어주고 다음의 범위를 탐색해봄
"""