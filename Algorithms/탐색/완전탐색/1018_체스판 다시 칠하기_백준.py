import sys

m, n = map(int, sys.stdin.readline().split())
chess_board = []
count = []

for _ in range(m):
    chess_board.append(sys.stdin.readline().strip())

for i in range(m-7):
    for j in range(n-7):
        count_w = 0
        count_b = 0
        
        for x in range(i, i+8):
            for y in range(j, j+8):
                current = chess_board[x][y]
                if (x+y)%2 == 0:
                    if current != 'W':
                        count_w += 1
                    if current != 'B':
                        count_b += 1
                else:
                    if current != 'B':
                        count_w += 1
                    if current != 'W':
                        count_b += 1
                        
        count.append(min(count_w, count_b))

print(min(count))

# 해당 문제는 8*8의 체스판을 어디서부터 잘라야 하는지(1)
# 체스판을 자른 후 체스판을 다시 칠해야 하는 경우(2)
# (1), (2)를 모두 직접 하나씩 탐색해야하는 완전탐색

# i, j 를 통해 자를 수 있는 체스판의 경우의 수를 모두 체크
# x, y를 통해 체스판을 자른 후 체스판을 다시 칠해야 하는 경우를 체크
# 색은 번갈아가면서 칠하므로, 일정한 규칙이 있음. 위치의 합이 짝수, 홀수로 나뉘는 규칙이 있으므로 %를 통해 나머지를 이용하여 문제 풀이 가능
