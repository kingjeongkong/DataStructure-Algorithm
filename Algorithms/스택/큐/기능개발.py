from collections import deque
from math import ceil

def solution(progresses, speeds):
    completion_days = deque()
    
    for p, s in zip(progresses, speeds):
        days = ceil((100 - p) / s)
        completion_days.append(days)
        
    answer = []
    
    if not completion_days:
        return answer
    
    current_max = completion_days.popleft()
    count = 1
    
    while completion_days:
        day = completion_days.popleft()
        
        if current_max >= day:
            count += 1
        else:
            answer.append(count)
            current_max = day
            count = 1
            
    answer.append(count)
            
    return answer


def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
