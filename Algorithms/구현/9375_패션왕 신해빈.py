import sys
from itertools import combinations

t = int(sys.stdin.readline())
for _ in range(t):
    category_dic = {}
    answer = 1
    n = int(sys.stdin.readline())
    for _ in range(n):
        cloth, category = sys.stdin.readline().split()
        category_dic[category] = category_dic.get(category, 1) + 1
        
    for v in category_dic.values():
        answer *= v
        
    print(answer - 1)

"""
이 문제는 수학을 이용한 구현 문제
처음에는 1~n까지의 각각의 조합을 combinations을 이용해서 구하고 반복문을 통해 각각에 대해 중복이 있는지 일일이 확인해봤음. 하지만 이렇게 하면 n개의 옷에 대해 각각 선택 or 노선택 두가지 경우의 수이므로 시간복잡도는 O(2^N)가 돼서 시간 초과가 됨

따라서 한번의 순회를 통해 답을 구해내야 함.
각 옷의 종류별로 하나씩만 입을 수 있으므로 종류별로 분류하면 됨. 그리고 각 종류의 옷을 선택하는 경우의 수를 곱해주면 됨.
n개의 옷을 순회할 때, 딕셔너리를 활용해서 옷의 종류의 개수를 증가해주면 됨. 그리고 옷을 안입는 경우의 수도 있으므로 각 종류별로 +1씩 해주고, 최종 결과에서 알몸인 상태 -1을 해주면 됨
"""