import sys

n, m = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
house_location = []
chicken_location = []


for y, city_row in enumerate(city):
    for x, val in enumerate(city_row):
        if val == 1:
            house_location.append((y, x))
        elif val == 2:
            chicken_location.append((y, x))
            
selected_chicken = []
min_city_dist = float('inf')

def backtrack(index):
    global min_city_dist
    
    if len(selected_chicken) == m:
        sum_dist = 0
        for house in house_location:
            city_dist = float('inf')
            for chicken in selected_chicken:
                house_y, house_x = house
                chicken_y, chicken_x = chicken
                y = abs(house_y - chicken_y)
                x = abs(house_x - chicken_x)
                if y+x < city_dist:
                    city_dist = y+x
            sum_dist += city_dist
        if sum_dist < min_city_dist:
            min_city_dist = sum_dist
        return
        
    for i in range(index, len(chicken_location)):
        selected_chicken.append(chicken_location[i])
        backtrack(i+1)
        selected_chicken.pop()

backtrack(0)
print(min_city_dist)

"""
해당 문제는 조합 or 백트래킹 문제 
백트래킹은 보통 모든 경우를 다 확인해야할 때(문제의 제약 조건이 작을 때), 한 선택이 다음 선택에 영향을 줄 때 사용
백트래킹이 사용되는 테마 예시로 다음과 같이 있음
- 조합 및 순열
- 경로 찾기(막다른 길일 경우 돌아감)
- 부분 집합 구하기(이거도 따지고 보면 조합)

이 문제도 결국 입력값이 매우 작기 때문에 모든 경우의 수를 확인해볼 수 있음
최대 M개의 치킨집을 골랐을 때의 조합들을 각각 구해서 각 집과의 치킨 거리를 각각 구해서 일일히 계산해서 더하면 됨.
조합을 구하는 과정에서 combination을 사용해도 되지만, 백트래킹을 사용해서 풀어봄
선택된 치킨들을 담을 리스트를 하나 생성한뒤 backtrack 함수 내에서 selected_chicken이 최대값 M개가 되면 치킨 거리를 계산함. 그렇지 않다면 재귀를 통해 selected_chicken을 채워나감. 
"""