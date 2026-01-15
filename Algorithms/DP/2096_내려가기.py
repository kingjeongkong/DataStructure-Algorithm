import sys

n = int(sys.stdin.readline())
first_line = list(map(int, sys.stdin.readline().split()))
max_dp = first_line[:]
min_dp = first_line[:]

for i in range(1, n):
    num = list(map(int, sys.stdin.readline().split()))
    
    
    max_zero = max(max_dp[0], max_dp[1]) + num[0]
    min_zero = min(min_dp[0], min_dp[1]) + num[0]
    
    max_one = max(max_dp) + num[1]
    min_one = min(min_dp) + num[1]
    
    max_two = max(max_dp[1], max_dp[2]) + num[2]
    min_two = min(min_dp[1], min_dp[2]) + num[2]
    
    max_dp = [max_zero, max_one, max_two]
    min_dp = [min_zero, min_one, min_two]

print(max(max_dp), end=" ")
print(min(min_dp))

"""
해당 문제는 DP 문제
한칸씩 내려갈 때마다 바로 아래 칸과 맞닿아 있는 칸만 선택 가능하므로, 규칙은 금방 찾을 수 있음.
관건은 메모리 초과.
메모리 할당량이 크지 않고 입력값이 1 ≤ N ≤ 100,000이므로 max_dp, min_dp, graph 리스트들을 각각 만들면 100,000 * 3 이므로 메모리 초과 발생.
이 문제에서 필요한건 현재 행의 값과 이전 행의 dp 값이므로 한 줄씩 입력 받아서 dp 값을 매번 업데이트 해주고 마지막 행의 값을 출력하면 됨.
"""