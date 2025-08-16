t = int(input())

for _ in range(t):
    n = int(input())
    
    dp_zero = [1, 0]
    dp_one = [0, 1]
    
    if n > 1:
        for i in range(2, n+1):
            dp_zero.append(dp_zero[i-1] + dp_zero[i-2])
            dp_one.append(dp_one[i-1] + dp_one[i-2])
    
    print(dp_zero[n], dp_one[n])

"""
피보나치 수에서 특정 수에 대해 0과 1이 호출되는 횟수를 구하는 문제

기존의 피보나치 수열 함수를 그대로 사용하면 시간 초과
-> 따라서 메모이제이션을 이용하여 호출 횟수를 줄여야 함.

이 과정에서 사용되는게 DP 문제 풀이 방법
n에 대한 피보나치 수는 n-1과 n-2에 대한 피보나치 수의 합으로 표현 가능
따라서 0과 1이 호출되는 횟수도 이를 활용 가능

n-1과 n-2에 대한 0과 1의 호출 횟수를 메모이제이션하여 효율적으로 문제 풀이
dp_zero, dp_one이라는 각각 n이라는 수에 대한 0과 1의 호출 횟수를 저장하는 배열 생성
n에 대한 수를 구할 때 dp_---[n-1] + dp_---[n-2]를 통해 호출 횟수를 구함
"""