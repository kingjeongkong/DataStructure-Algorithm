import sys

n = int(sys.stdin.readline())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[] for _ in range(n)]
dp[0].append(triangle[0][0])

for layer_ind, x in enumerate(triangle[1:], start=1):
    for num_ind, y in enumerate(x):
        if num_ind == 0:
            dp[layer_ind].append(dp[layer_ind-1][0] + y)
            continue
        if num_ind == layer_ind:
            dp[layer_ind].append(dp[layer_ind-1][num_ind-1] + y)
            continue
            
        dp[layer_ind].append(max(dp[layer_ind-1][num_ind-1] + y, dp[layer_ind-1][num_ind] + y))

print(max(dp[n-1]))

"""
해당 문제는 DP 문제
삼각형의 맨 위층부터 차례대로 아래층으로 내려오면서 선택된 수들의 합 중에서 최대를 구하는 문제
이전의 선택이 이후의 선택에 영향을 미치고, 이전의 선택된 값들을 메모이제이션 해뒀다가 재사용해서 풀어야 하므로 DP로 접근
아래층으로 내려갈수록 선택할 수 있는 경우가 늘어나므로, dp를 2차원 배열로 만듦
이후 인덱스 오류를 예방하기 위해 각 층의 0번 인덱스와 마지막 인덱스는 각각 이전 층의 0번 인덱스와 마지막 인덱스의 값을 더해서 저장하는 방식으로 따로 처리해줌.
그리고 나머지 인덱스는 이전층의 각 인덱스에서 선택할 수 있는 경우의 수 중에서 최대값을 더해서 저장하는 방식으로 풀이.
"""