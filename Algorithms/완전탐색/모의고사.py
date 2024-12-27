from math import ceil

def solution(answers):
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = [0, 0, 0]
    
    def multiple(arr):
        if len(answers)/len(arr) > 1:
            multipleArr = arr*(ceil(len(answers)/len(arr)))
            return multipleArr
        else:
            return arr
            
    num1 = multiple(num1)
    num2 = multiple(num2)
    num3 = multiple(num3)
    
    for index, answer in enumerate(answers):
        if num1[index] == answer:
            result[0] += 1
        if num2[index] == answer:
            result[1] += 1
        if num3[index] == answer:
            result[2] += 1
            
    max_score = max(result[0], result[1], result[2])
    winner = []
    
    if result[0] == max_score:
        winner.append(1)
    if result[1] == max_score:
        winner.append(2)
    if result[2] == max_score:
        winner.append(3)
    
    return winner

"""
개선점

    def multiple(arr):
        if len(answers)/len(arr) > 1:
            multipleArr = arr*(ceil(len(answers)/len(arr)))
            return multipleArr
        else:
            return arr
            
    num1 = multiple(num1)
    num2 = multiple(num2)
    num3 = multiple(num3)
    
    for index, answer in enumerate(answers):
        if num1[index] == answer:
            result[0] += 1
        if num2[index] == answer:
            result[1] += 1
        if num3[index] == answer:
            result[2] += 1

다음 코드에서 num1,2,3의 배열을 늘리는게 아니라 %를 활용하여 나머지 값으로 해결

    for index, answer in enumerate(answers):
        if answer == num1[index%len(num1)]:
            result[0] += 1
        if answer == num2[index%len(num2)]:
            result[1] += 1
        if answer == num3[index%len(num3)]:
            result[2] += 1


그리고 
    max_score = max(result[0], result[1], result[2])
    winner = []
    
    if result[0] == max_score:
        winner.append(1)
    if result[1] == max_score:
        winner.append(2)
    if result[2] == max_score:
        winner.append(3)

이 코드에서 배열은 max로 한번에 비교 가능
    winner = []
    for i in range(len(result)):
        if result[i] == max(result):
            winner.append(i+1)

    or

    for index, value in enumerate(result):
        if value == max(result):
            winner.append(index+1)
"""