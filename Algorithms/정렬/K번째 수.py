def solution(array, commands):
    n = len(commands)
    
    sorted_array = []
    answer = []
    
    for i in range(n):
        sorted_array.append(array[commands[i][0] - 1 : commands[i][1]])
        sorted_array[i].sort()
        answer.append(sorted_array[i][commands[i][2] - 1])
    
    return answer
    

def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command
        sliced_array = array[i-1:j]
        sorted_array = sorted(sliced_array)
        answer.append(sorted_array[k-1])
    
    return answer