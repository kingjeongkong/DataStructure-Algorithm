import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)
answer = 0

for coin in coins:
    if k//coin != 0:
        answer += k//coin
        k -= coin * (k//coin)
        
    if k == 0:
        break
        
print(answer)

"""
그리디 알고리즘 문제

최소한의 동전 개수를 사용해서 원하는 금액을 만들어야 하므로 높은 금액의 동전을 먼저 활용.
이 문제는  1, 5, 10, 50, 100...처럼 항상 큰 단위가 작은 단위의 배수라는 특별한 조건이 있기에 쉽게 풀렸음.

근데 동전 단위가 {1, 3, 4}이고 6원을 거슬러 줘야 한다면, 그리디 방식(4원짜리 1개, 1원짜리 2개 = 총 3개)은 최적의 해(3원짜리 2개 = 총 2개)가 아니기 때문에 다른 방식으로 풀어야 함.
이럴 경우 더 고민해봐야할 필요가 있을듯 
"""