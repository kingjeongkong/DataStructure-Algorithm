import sys

n = int(input())
p = list(map(int, sys.stdin.readline().split()))
p.sort()
answer = 0

for i in range(n):
    for j in range(0, i+1):
        answer += p[j]

print(answer)

"""
해당 문제는 그리디 알고리즘 문제
돈 인출하는데 걸리는 시간을 모든 사람을 합하여 최솟값을 만들어야 함.
앞의 사람이 인출하는데 시간이 조금 걸려야 대기 시간도 줄어듦
따라서 인출 시간을 오름차순으로 정렬한 후 각 사람의 시간을 모두 합하면 됨
"""