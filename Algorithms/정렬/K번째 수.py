def solution(array, commands):
    n = len(commands)
    
    sorted_array = []
    answer = []
    
    for i in range(n):
        sorted_array.append(array[commands[i][0] - 1 : commands[i][1]])
        sorted_array[i].sort()
        answer.append(sorted_array[i][commands[i][2] - 1])
    
    return answer