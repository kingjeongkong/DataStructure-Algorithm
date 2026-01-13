import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w_i, v_i = map(int, sys.stdin.readline().split())
    for w in range(1, k+1):
        if w >= w_i:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-w_i] + v_i)
        else:
            dp[i][w] = dp[i-1][w]

print(max(dp[n]))

"""
해당 문제는 dp 문제
dp 문제를 풀 때는 문제의 제약 조건을 dp의 인덱스로 설정 (이 문제는 물건, 무게를 인덱스로 설정), 최종 구해야 하는 값은 dp의 값으로 설정
각 물건들에 대해서 넣는 경우, 안넣는 경우를 비교
만약 인덱스의 무게(반복문으로 1부터 최대 무게까지 비교)가 물건의 무게보다 크다면 넣는 경우(dp[i-1][w-w_i] 이전 물건에 대해 처리한 경우의 수들 중에서 현재 해당 물건의 무게를 뺀 경우의 수의 값)과 안넣는 경우(dp[i-1][w])을 비교해서 더 큰 값을 dp에 저장
만약 물건의 무게가 인덱스의 무게보다 크다면 안넣는 경우의 값을 dp에 저장
이후 결과값으로 dp의 마지막 층에서 최대 가치를 가지는 값을 출력
"""