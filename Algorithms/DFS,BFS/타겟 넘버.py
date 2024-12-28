answer = 0

def dfs(numbers, target, current, index):
    global answer
    
    if index == len(numbers):
        if current == target:
            answer += 1
        return
    
    dfs(numbers, target, current + numbers[index], index+1)
    dfs(numbers, target, current - numbers[index], index+1)

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer


# BFS
from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0)])
    answer = 0
    
    while queue:
        current_sum, index = queue.popleft()
        
        if index == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            queue.append((current_sum + numbers[index], index+1))
            queue.append((current_sum - numbers[index], index+1))
    
    return answer