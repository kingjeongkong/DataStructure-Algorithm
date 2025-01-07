input = [int(input()) for _ in range(9)]

def solution(input):
    dwarf_num = len(input)
    sum = 0
    for i in input:
        sum += i

    for i in range(dwarf_num):
        for j in range(i+1, dwarf_num):
            liar1 = input[i]
            liar2 = input[j]
            if (sum - liar1 - liar2) == 100:
                input.remove(liar1)
                input.remove(liar2)
                return sorted(input)

answer = solution(input)
for i in answer:
    print(i)