def solution(arr):
    answer = []
    prev = None
    
    for i in arr:
        if i != prev:
            answer.append(i)
            prev = i
            
    return answer
    

def solution(arr):
    stack = []
    
    for i in arr:
        if not stack:
            stack.append(i)
        elif stack[-1] != i:
            stack.append(i)
            
    return stack