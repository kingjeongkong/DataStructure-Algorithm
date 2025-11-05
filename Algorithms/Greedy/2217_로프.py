n = int(input())
rope_list = [int(input()) for _ in range(n)]
rope_list.sort()
answer = []

for i, rope in enumerate(rope_list):
    answer.append(rope * (len(rope_list) - i))
    
print(max(answer))

"""
해당 문제는 그리디 문제
모든 로프를 사용 안하고 임의의 몇개만 사용해도 되므로, 각각의 로프를 사용하는 경우의 수를 모두 고려해야 함.
"""