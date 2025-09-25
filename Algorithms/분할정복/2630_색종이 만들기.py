import sys

n = int(sys.stdin.readline())
square = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
white = 0
blue = 0

def solve(y, x, n):
    global white, blue
    start_color = square[y][x]
    for j in range(y, y+n):
        for i in range(x, x+n):
            if square[j][i] == start_color:
                continue
            else:
                new_n = n // 2
                solve(y, x, new_n)
                solve(y + new_n, x, new_n)
                solve(y, x + new_n, new_n)
                solve(y + new_n, x + new_n, new_n)
                return
    if start_color == 0:
        white += 1
    else:
        blue += 1

solve(0, 0, n)
print(white)
print(blue)

"""
처음의 정사각형에서 모두 같은 색이 아니면 4등분해서 각각의 영역이 같은 색인지 확인
-> 이 과정을 같은 색일때까지 반복 -> 재귀를 사용
재귀를 사용해야하기에 dfs 문제인줄 알았으나 한칸씩 인접한 곳으로 가는 것이 아닌 하나의 문제를 여러 개로 분할해서 다시 그 문제들을 따지는 것이므로 분할정복

y, x 시작점의 색깔을 알아내서 같은 영역의 색깔이 모두 같은지 확인 -> 같다면 반복문을 빠져나와서 같은 색의 개수를 추가
같지 않다면 4등분해서 각각의 영역들이 같은 색인지 각각 확인 -> 재귀 함수 사용 -> 관건은 시작점(y, x)와 너비(n)을 어떻게 설정할지
분할을 해야할 때 너비를 절반으로 줄여야 하므로 n // 2로 설정 -> n이 1이 되면 같은 색 조건 바로 만족하므로 따로 조건문 처리 안해줘도 됨
"""