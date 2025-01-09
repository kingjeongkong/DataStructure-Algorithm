def solution(participant, completion):
    for c in completion:
        participant.remove(c)
        
    return participant[0]

# 위의 풀이는 정답은 맞지만 효율성 테스트에서 실패함
# participant 값이 100,000이하, remove 함수의 시간복잡도가 O(N)이므로 for과 합쳐지면 O(N^2) 시간 초과 -> 딕셔너리로 풀어야함.

def solution(participant, completion):
    participant_dict = {}

    for p in participant:
        participant_dict[p] = participant_dict.get(p, 0) + 1

    for c in completion:
        if participant_dict[c] == 1:
            del participant_dict[c]
        else:
            participant_dict[c] = participant_dict.get(c) - 1

    return list(participant_dict.keys())[0]