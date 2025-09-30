import sys

n, m = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0]
for num in n_list:
    prefix_sum.append(prefix_sum[-1] + num)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(prefix_sum[j] - prefix_sum[i-1])

"""
이 문는 N개의 수 리스트에서 총 M번의 구간 합을 구해야 하는 문제
일반적으로 문제를 풀면 각 M번의 구간 합마다 N개의 수를 반복문으로 더해주면 됨 하지만 N, M의 입력값의 최대값은 100,000으로 시간복잡도는 O(N*M)이므로 시간 초과

시간을 최적화해야 하므로 누적합을 사용.
누적합 배열을 구할 때는 한번 순회해야 하므로 O(N)의 시간 복잡도가 필요하지만 한번 순회하면 이후에는 단순 계산만 해주면 되기에 O(1)의 시간 복잡도가 필요
"""