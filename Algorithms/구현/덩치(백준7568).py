import sys

num_people = int(sys.stdin.readline())
weight_height = [list(map(int, sys.stdin.readline().split())) for _ in range(num_people)]

def compare(num, weight_height):
    rank = [1 for _ in range(num)]
    
    for i in range(num):
        for j in range(i+1, num):
            f_weight, f_height = weight_height[i]
            s_weight, s_height = weight_height[j]
            
            if f_weight > s_weight and f_height > s_height:
                rank[j] += 1
            elif f_weight < s_weight and f_height < s_height:
                rank[i] += 1
                
    return rank


print(*compare(num_people, weight_height))

#print에서 리스트나 튜플의 각 요소를 공백으로 구분하여 출력하기 위해서는 *(언패킹 연산자(unpacking operator)) 사용해야 함