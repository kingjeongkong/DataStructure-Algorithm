num = int(input())
test_array = [int(input()) for _ in range(num)]

def solution(input):
    if input == 1:
        return 1
    elif input == 2:
        return 2
    elif input == 3:
        return 4
    
    answer = solution(input-3) + solution(input-2) + solution(input-1)
    
    return answer

for input in test_array:
    print(solution(input))

# DP 문제 - 최종 테스트 케이스 값을 구하기 위해서 그 하위 값들의 합을 더해서 도출
# -> Top-Down으로 접근
"""
총 사용할 수 있는 수는 1, 2, 3
따라서 n을 만들기 위해서는
n-1을 만들고 +1 해주면 되므로 (n-1)을 만드는 개수
n-2를 만들고 +2 해주면 되므로 (n-2)을 만드는 개수
n-3을 만들고 +3 해주면 되므로 (n-3)을 만드는 개수
의 합

따라서 점화식은 
dp(n) = dp(n-1) + dp(n-2) + dp(n-3)

n이 1,2,3일 경우는 각각 구해서 처리.
"""