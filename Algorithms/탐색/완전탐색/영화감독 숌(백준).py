input = int(input())

def solution(input):
    num = 666
    count = 1
    
    while count!=input:
        num += 1
            
        if '666' in str(num):
            count += 1
            
    return num

print(solution(input))