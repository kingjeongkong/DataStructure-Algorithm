from collections import deque

n = int(input())
num_list = deque()
stack_list = deque()
answer = []
for _ in range(n):
    num_list.append(int(input()))

for i in range(1, n+1):
    stack_list.append(i)
    answer.append("+")
    
    while num_list and stack_list and num_list[0] == stack_list[-1]:
        num_list.popleft()
        stack_list.pop()
        answer.append("-")

if len(num_list) == 0:
    for i in answer:
        print(i)
else:
    print("NO")

"""
입력값인 수열을 num_list에 저장
이후 1부터 n까지 숫자를 차례대로 stack에 넣는 것처럼 stack_list에 넣음.
매 수마다 num_list의 첫번째 값이 stack_list의 마지막 값(스택이므로)과 같은지 확인하고 같으면 pop함. -> while를 통해 연속으로 pop되어야 하는 숫자들도 확인 가능

n까지의 숫자를 모두 stack에 넣고 반복문이 끝난 후 num_list가 비어있으면 입력된 배열 생성 가능, 아니면 불가능(NO 출력)
"""