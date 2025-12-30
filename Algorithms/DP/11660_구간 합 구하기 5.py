import sys

n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
pre_sum = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        pre_sum[i][j] = table[i-1][j-1] + pre_sum[i][j-1] + pre_sum[i-1][j] - pre_sum[i-1][j-1]
        
for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(pre_sum[x2][y2] - pre_sum[x2][y1-1] - pre_sum[x1-1][y2] + pre_sum[x1-1][y1-1])

"""
해당 문제는 구간합을 구하는 문제
(x1, y1) ~ (x2, y2)의 구간합을 일일이 모두 구해서 메모이제이션 해놓는 방식은 매우 복잡해지므로 (1, 1) ~ (x2, y2)의 구간합을 메모이제이션 해놓고 불필요한 구간들을 빼는 방식으로 풀이 -> pre_sum 배열을 2차원 배열로 생성

이후 pre_sum 배열을 채워야 함
초기에 생각은 일일이 더해서 구해보려고 했으나 그럼 for문이 4번 중첩돼서 시간 초과 발생
-> 따라서 누적합을 이용해서 구해줌
그리고 인덱스를 0부터 하는 것이 아닌 좌표 계산하기 편하게 1부터 시작하도록 함. 또한 인덱스 0들에는 패딩(0으로 감싸는 한줄)을 추가해서 인덱스 오류를 방지

이후 (x1, y1) ~ (x2, y2) 구간합을 구할 때 (x2, y2)까지의 구간합에서 (x1-1, y2)까지의 구간합과 (x2, y1-1)까지의 구간합을 빼주고 (x1-1, y1-1)까지의 구간합을 더해줌으로써 구간합을 구함
인덱스 0은 패딩으로 감싸져 있으므로 따로 인덱스 분기처리를 하지 않아줘도 인덱스 오류 뜨지 않음
"""