"""
첫번째 풀이는 소괄호 대괄호 각각 점수를 만들어서 
두번째 풀이는 괄호에 대해서 balanced라는 Boolean으로 처리
"""

def solution():
    sentence = str(input())
    stack = []
    round_bracket = 0
    square_bracket = 0
    
    while sentence != '.':
        for i in sentence:
            if i == '(':
                round_bracket += 1
                stack.append(i)
            elif i == ')':
                round_bracket -= 1
                if not stack or stack.pop() != '(':
                    break
            elif i == '[':
                square_bracket += 1
                stack.append(i)
            elif i == ']':
                square_bracket -= 1
                if not stack or stack.pop() != '[':
                    break
                
            if round_bracket < 0:
                break
            elif square_bracket < 0:
                break
                
        if round_bracket == 0 and square_bracket == 0:
            print('yes')
        else:
            print('no')
        
        round_bracket = 0
        square_bracket = 0
        stack = []
        sentence = str(input())
        
solution()


def solution():
    while True:
        sentence = input()
        stack = []
        balanced = True
        
        if sentence == '.':
            return
        
        for i in sentence:
            if i == '(' or i == '[':
                stack.append(i)
            elif i == ')':
                if not stack or stack[-1] != '(':
                    balanced = False
                    break
                else:
                    stack.pop()
            elif i == ']':
                if not stack or stack[-1] != '[':
                    balanced = False
                    break
                else:
                    stack.pop()
                
        if not stack and balanced:
            print('yes')
        else:
            print('no')
            
    
solution()