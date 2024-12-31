from collections import deque

def solution():
    inputt = input()
    input_list = deque([i for i in inputt])
    stack = []
    queue = deque([])
    
    while True:
        if not input_list:
            break
            
        char = input_list.popleft()
        
        if char == '<':
            while stack:
                print(stack.pop(), end='')
            queue.append(char)
        elif char == '>':
            while queue:
                print(queue.popleft(), end='')
            print(char, end='')
        elif char == ' ':
            if queue:
                queue.append(char)
            elif stack:
                while stack:
                    print(stack.pop(), end='')
                print(char, end='')
        else:
            if queue:
                queue.append(char)
            else:
                stack.append(char)
            
            
    while stack:
        print(stack.pop(), end='')
        

        
solution()