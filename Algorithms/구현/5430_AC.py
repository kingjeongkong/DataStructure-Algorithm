import sys
from collections import deque

t = int(sys.stdin.readline().strip())

for _ in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()[1:-1]
    
    if n == 0:
        num_list = deque()
    else:
        num_list = deque(s.split(','))
    
    reversed_bool = False
    
    for rd in p:
        if rd == 'R':
            reversed_bool = not reversed_bool
        elif rd == 'D':
            if num_list:
                if reversed_bool:
                    num_list.pop()
                else:
                    num_list.popleft()
            else:
                print('error')
                break
    else:
        if reversed_bool:
            num_list.reverse()
        print(f"[{','.join(num_list)}]")


"""
해당 문제는 단순 구현 문제
단순하게 문제의 요구사항대로 입력값을 받아서 R, D 함수를 실행하면 될 수도 있겠지만,
이 문제는 함수 p의 입력값이 100,000이하이고 배열 안의 수의 개수도 100,000이하이므로 단순하게 실행하면 O(N^2)이므로 시간초과 발생(reverse 함수 O(N), pop은 deque를 사용한다면 O(1))
D 함수는 가장 앞의 수를 버리는 것이므로, 직접 reverse를 하기보다는 reverse 여부를 파악해서 deque를 사용해서 popleft를 할건지 pop를 할건지 판단하여 실행할 수 있음

코드 작성에서 [1,2,3,4] 다음과 같은 입력값을 리스트로 만들어야할 때 [1:-1]과 같이 슬라이싱을 통해 []를 제외하고 입력값 추출 후 split(',')을 통해 리스트로 만들 수 있음
그리고 for else 구문을 사용하여 break 없이 모든 함수를 실행했을 때 예외처리를 할 수 있음
또한 n==0인 경우 deque를 빈 배열로 초기화하여 예외처리 가능, 그렇지 않으면 deque에 '' 값이 들어갈 수 있음
"""