import sys

n, r, c= map(int, sys.stdin.readline().split())

def solution(n, row, col):
    if n == 0:
        return 0
    
    half = 2 ** (n-1)
    quadrant_size = half * half
    
    if row < half and col < half:
        return solution(n-1, row, col)
    elif row < half and col >= half:
        return quadrant_size + solution(n-1, row, col - (2 ** (n-1)))
    elif row >= half and col < half:
        return 2 * quadrant_size + solution(n-1, row - (2 ** (n-1)), col)
    else:
        return 3 * quadrant_size + solution(n-1, row - (2 ** (n-1)), col - (2 ** (n-1)))

print(solution(n, r, c))


"""
해당 문제는 분할정복 문제

처음 문제를 보고 Z가 반복되므로 재귀를 사용하고 큰 Z내에서 작은 Z들을 쪼개서 풀어야 한다고 생각함.
재귀를 사용하는 문제는 DFS도 있고, 큰 문제를 작게 쪼개서 푸는 문제는 DP도 있으므로 어떤 방식을 써야할 지 감이 잘 잡히지 않았음.
문제를 쪼개서 풀어야 할 때 :
- 하위 문제들이 서로 중첩됨 -> DP
- 하위 문제들이 독립적임 -> 분할 정복
재귀를 사용해서 풀어야 할 때 :
- 현재 위치에서 인접한 다음 칸으로 이동하는가(연결된 덩어리 찾기인가) -> DFS
- 그냥 영역을 분할하는건가 -> 분할 정복

직접 순회하면서 r, c의 위치를 찾아보려고 했으나 N이 15이면 2^15 * 2^15 = 2^30 = 10억 이므로 시간 초과가 발생함.
Z를 크게 4개의 사분면으로 나눈다면, r,c가 있는 사분면 이전의 사분면들은 따로 탐색 없이 크기를 바로 더해주면 됨.
이 방식을 n이 0일 때까지 반복해주면 됨. n이 0이 될 때는 r, c의 위치이기 때문.
행, 열을 반절로 잘라서 다음 재귀를 위한 범위 half는  2^(n-1)
r,c 이전의 사분면들의 크기는 quadrant_size로 바로 더해줌
"""