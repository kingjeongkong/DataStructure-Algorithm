import sys

k, n = map(int, sys.stdin.readline().split())
lan_list = [int(sys.stdin.readline()) for _ in range(k)]
start = 1
end = max(lan_list)
answer = 0

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for lan in lan_list:
        sum += lan // mid
    
    if sum >= n:
        answer = mid
        start = mid + 1
    elif sum < n:
        end = mid - 1

print(answer)

"""
이 문제는 나무 자르기와 비슷한 문제
k개의 랜선을 가지고 n개의 동일한 길이의 랜선을 만들어야 하는 문제 (k<=n)
k와 n의 입력값은 각각 1<=k<=10,000, 1<=n<=1,000,000 이고 n개의 랜선을 만드는 최대 길이를 구하는 문제이므로 이진 탐색이 적절 ("매우 큰 범위 안에서 특정 조건을 만족하는 최댓값을 찾아라"는 요구는 이진 탐색을 떠올려야 함)

따라서 start(랜선을 자르고 몫을 가져가야 하므로 // 연산을 해야함, divisor는 0이 되면 안되므로 start를 1부터 시작), end 값을 설정해주고 이진 탐색 시작
"""