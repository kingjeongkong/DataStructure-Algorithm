import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    
    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
        continue
        
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    dp[0][1] = sticker[1][0] + sticker[0][1]
    dp[1][1] = sticker[0][0] + sticker[1][1]
    
    for i in range(2, n):
        dp[0][i] = sticker[0][i] + max(dp[1][i-2], dp[1][i-1])
        dp[1][i] = sticker[1][i] + max(dp[0][i-2], dp[0][i-1])
        
    print(max(dp[0][n-1], dp[1][n-1]))

"""
해당 문제는 DP 문제
각각의 스티커들을 선택해서 최대의 점수를 만들어야 함.
이전의 선택이 이후의 선택에 영향을 미치고, 이전의 선택된 값들을 메모이제이션 해뒀다가 재사용해서 풀어야 하므로 DP로 접근
현재 선택의 위치와 값을 저장해야하므로 dp를 2차원 배열로 만듦
그리고 이전의 메모이제이션을 재사용하는 것은 대각선의 한칸의 열 뒤랑 2칸의 열 뒤의 값을 활용하면 됨
"""