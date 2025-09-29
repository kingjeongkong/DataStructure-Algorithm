import sys

n, m = map(int, sys.stdin.readline().split())
n_list = {sys.stdin.readline().strip() for _ in range(n)}
m_list = {sys.stdin.readline().strip() for _ in range(m)}
common = []

for i in n_list:
    if i in m_list:
        common.append(i)

print(len(common))
for i in sorted(common):
    print(i)

"""
이 문제는 단순 구현
입력값이 각각 500,000이하면서 중복되는 요소를 찾아야 하는 것.
빠른 탐색을 통해 시간 복잡도를 낮추는게 관건인 문제
따라서 set을 사용하여 탐색 시간을 O(1)로 줄임
"""