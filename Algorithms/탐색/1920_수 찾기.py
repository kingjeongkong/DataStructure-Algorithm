import sys

n = int(sys.stdin.readline())
n_array = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_array = list(map(int, sys.stdin.readline().split()))

for i in m_array:
    if i in n_array:
        print("1")
    else:
        print("0")


"""
해당 문제는 '정수의 범위는 -231 보다 크거나 같고 231보다 작다'이므로 시간복잡도를 줄이는게 관건
단순히 list를 사용해 탐색을 하면 시간 복잡도는 O(N*M)이므로 시간 초과가 발생함
-> 따라서 set을 사용하여 탐색 시간을 O(1)로 줄임

or
이진 탐색을 사용하여 탐색 시간을 O(logN)으로 줄일 수 있음
"""