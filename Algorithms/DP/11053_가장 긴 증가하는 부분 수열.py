import sys

n = int(sys.stdin.readline())
list_a = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

for i in range(n):
    for j in range(0, i):
        if list_a[i] > list_a[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

"""
해당 문제는 DP를 이용해서 푸는 문제
현재의 선택이 이전의 수보다 크면 이전의 수의 수열 최대 길이에 +1만 해주면 되므로 이전의 수들의 수열 최대 길이들을 기억해뒀다가 재활용해서 사용하면 되므로 dp를 이용.
"""