# 문자열을 비교할 때 맨 앞자리부터 비교함. 앞자리가 크면 큰 것 (숫자 앞자리가 크면 큰 것이 큼)
# 3, 30 과 같은 경우 앞자리가 3으로 똑같아서 30, 3 으로 정렬됨
# 해당 문제는 1000이하의 숫자이므로 3자리 수, str(숫자)에 3을 곱해서 한자리 수도 3자리로 만들어 각 자리 수 비교할 수 있게 함.
# sort 함수에서 lambda 함수를 사용해서 3자리 수를 곱해서 reverse로 정렬하고
# 예외 케이스 [0, 0, 0]이면은 값은 000이 됨. 이 경우에는 str(int(000))로 0이 됨


def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key=lambda x: x*3, reverse=True)
    answer = ''.join(str_numbers)
    
    # if answer[0] == '0':
    #     return '0'
    
    # return answer

    return str(int(answer))