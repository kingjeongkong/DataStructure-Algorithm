import sys

n = int(sys.stdin.readline())
tanghuru = list(map(int, sys.stdin.readline().split()))
start = 0
fruit = {}
answer = 0

for end in range(n):
    fruit[tanghuru[end]] = fruit.get(tanghuru[end], 0) + 1
    if len(fruit) >= 3:
        while len(fruit) >= 3:
            fruit[tanghuru[start]] -= 1
            if fruit[tanghuru[start]] == 0:
                del fruit[tanghuru[start]]
            start += 1
            
    if answer < end - start + 1:
        answer = end - start + 1

print(answer)

"""
처음 문제의 접근으로는 '과일의 개수가 가장 많은 탕후루의 과일 개수'를 구해야 했으므로 최적의 해를 찾는 문제인줄 알고 그리디로 접근.
과일 종류에 따른 개수를 핸들링해야 하므로 딕셔너리를 떠올림. 하지만 과일을 뺄 때 앞에서 뺄지 뒤에서 뺄지에 대한 기준을 세우지 못하겠음.
찾아보니 투 포인터로 풀어야 한다는걸 꺠달음

입력값은 N이 200,000까지 가능하므로 시간 복잡도가 O(N) or O(NlogN)으로 풀어야 함
또한 과일들은 연속되어 있음(부분 배열을 구해야 하는 것)
연속된 부분 배열을 탐색하는 알고리즘 = 투 포인터
투 포인터는 두 개의 포인터(start, end)를 사용해 end를 먼저 늘려가며 구간을 확장하고 조건에 만족하지 않는 배열이 나오면 start를 늘려가며 조건을 맞춰가며 부분 배열을 탐색해가는 방식

이 문제도 start, end 두 개의 포인터를 0부터 시작해서 end을 +1 해주면서 딕셔너리를 활용해서 과일의 종류가 2개 이하인지 계속해서 추적하면서 과일을 추가해줌.
만약 과일의 종류가 3개 이상이 된다면 종류가 2개 이하가 될 때까지 start를 +1 해주며 조건이 맞을 때까지 과일을 빼주며 반복문을 돌려줌.
각 부분 배열들에 대해 과일 개수를 비교하면서 가장 많은 과일 개수를 찾아내면 됨.
"""