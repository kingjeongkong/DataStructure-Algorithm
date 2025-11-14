import sys

n, m, b = map(int, sys.stdin.readline().split())
map_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer_list = []

for i in range(257):
    temp_b = b
    time = 0
    
    for y in range(n):
        for x in range(m):
            gap = abs(i - map_list[y][x])
            if i > map_list[y][x]:
                time += gap
                temp_b -= gap
            elif i < map_list[y][x]:
                time += 2 * gap
                temp_b += gap
                
    if temp_b >= 0:
        answer_list.append((time, i))
        
answer = min(answer_list, key=lambda x: (x[0], -x[1]))
print(answer[0], answer[1])

"""
최소 시간을 구하는 문제이기에 BFS, DP, 그리디를 떠올림
BFS로 풀기에는 최단 경로나 그룹과 같은 덩어리, 그래프적 연결성이 아니기에 제외
DP로 풀기에는 각각이 독립적인 계산이므로 제외
그리디로 풀기에는 최적의 선택들이 반례가 존재해서, 최적의 해를 보장 못해서 제외

입력값의 범위가 높이는 0~256, 땅의 가로 세로 개수는 0~500이므로 총 256*500*500 = 64,000,000번의 연산이므로 완전탐색으로 접근 가능
"""