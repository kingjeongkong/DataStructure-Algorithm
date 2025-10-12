import sys

n = int(sys.stdin.readline())
x_list = list(map(int, sys.stdin.readline().split()))
x_set = set(x_list)
x_sorted_list = sorted(x_set)
x_dict = dict()

for i, x in enumerate(x_sorted_list):
    x_dict[x] = i

for x in x_list:
    print(x_dict[x], end=" ")

"""
해당 문제는 특정 x의 값보다 작은 값의 개수를 찾아서 출력하는 문제
단순하게 생각하면 모든 각 x의 값마다 순회를 하면서 작은 값의 개수를 직접 세면 됨
-> 하지만 다음과 같이 하면 시간 복잡도는 O(N^2)가 되고 입력값인 N이 1,000,000이므로 시간 초과

중복을 제거하고 오름차순으로 정렬하면 해당 x의 인덱스가 해당 x의 값보다 작은 값의 개수가 됨
set를 활용해 중복 제거, sorted를 활용해 오름차순 정렬
딕셔너리를 활용해서 x의 인덱스 값 빠르게 찾음 -> 딕셔너리를 사용하지 않고 정렬된 리스트에서 .index()를 활용하면 O(N)의 시간 복잡도가 되므로 모든 x의 값을 찾는데 O(N^2)의 시간 복잡도가 되므로 시간 초과
"""