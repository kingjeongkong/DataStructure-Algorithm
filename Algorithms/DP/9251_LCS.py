import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
print(dp[len(s1)][len(s2)])

"""
해당 문제는 DP 문제
연속적인 부분 수열을 찾는 것이 아닌 부분 수열을 찾는 문제
가장 길게 만드려면 이전의 선택이 이후의 선택에 영향을 미치고, 이전의 선택된 값들을 메모이제이션 해뒀다가 재사용해서 풀어야 하므로 DP로 접근
변화하는 값은 문자열 2개이므로 dp를 2차원 배열로 만듦
행, 열을 각각 문자열로 두고 각 인덱스를 문자열의 문자 하나씩으로 둠.
for문을 통해서 문자 2개를 비교해서 같으면 두 문자열의 바로 이전값([i-1][j-1])에 +1를 해줌
문자 2개가 다르면 각각 두 문자를 비교하기 이전의 값에서 최대값을 찾아서 해당 값에 저장
"""