import sys

num_list = list(sys.stdin.readline().split("-"))
answer = 0

for index, num in enumerate(num_list):
    a = 0
    if "+" in num:
        plus_list = list(num.split("+"))
        plus_sum = 0
        for plus_num in plus_list:
            plus_sum += int(plus_num)
        a = plus_sum
    else:
        a = int(num)
        
    if index == 0:
        answer += a
    else:
        answer -= a

print(answer)

"""
        plus_list = list(num.split("+"))
        plus_sum = 0
        for plus_num in plus_list:
            plus_sum += int(plus_num)
        a = plus_sum
는 a = sum(map(int, num.split('+'))) 처럼 한줄로 줄일 수 있음

해당 문제는 최솟값을 구해야 하는 최적화 문제 -> DP나 그리디를 떠올릴 수 있음
수식의 결과를 최소로 만들기 위해서는 뺄셈에서 가장 큰 값을 빼주는게 최적의 해가 됨
그럼 -뒤에 나오는 +연산에서 괄호를 묶어 모두 더해줘서 큰 값을 만들어 주면 됨
이렇게 -뒤에 오는 +연산들을 괄호로 묶어주는건 독립된 선택들임 -> 그리디 알고리즘 문제

따라서 풀이는 -를 기준으로 연산들을 분리해줌 split("-")
이후 분리된 연산들을 각각 처리해줌(+ 연산이 있는 경우 +를 기준으로 분리해서 split("+") 각 숫자들을 더해줌)
그리고 첫번째 연산은 더해주고 나머지 연산은 빼줘서 최솟값을 구함
"""