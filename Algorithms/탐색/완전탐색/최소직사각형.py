# 명함을 돌릴 수 있음. 가로에 큰 값이 가게 하고 세로에 작은 값이 가게 함
# 가로 = 큰 값 중에서 가장 큰 값, 세로 = 작은 값 중에서 가장 큰 값
# 이렇게 하면 모든 명함 포함 가능

def solution(sizes):
    width = 0
    height = 0
    
    for size in sizes:
        x, y = size
        
        if width < max(x, y):
            width = max(x, y)
        if height < min(x, y):
            height = min(x, y)
            
    return width * height