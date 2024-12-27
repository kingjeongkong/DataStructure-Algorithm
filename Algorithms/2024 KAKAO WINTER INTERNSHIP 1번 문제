def solution(friends, gifts):
    # 1. 친구 목록을 인덱스에 매핑
    friend_to_index = {friend: idx for idx, friend in enumerate(friends)}
    n = len(friends)
    
    # 2. 선물 주고받은 횟수를 저장할 2차원 리스트 초기화
    gift_matrix = [[0] * n for _ in range(n)]
    
    # 각 친구가 준 선물과 받은 선물의 수를 저장할 리스트 초기화
    gift_given = [0] * n
    gift_received = [0] * n
    
    # 선물 기록을 처리
    for record in gifts:
        giver, receiver = record.split()
        giver_idx = friend_to_index[giver]
        receiver_idx = friend_to_index[receiver]
        gift_matrix[giver_idx][receiver_idx] += 1
        gift_given[giver_idx] += 1
        gift_received[receiver_idx] += 1
    
    # 3. 선물 지수 계산
    gift_index = [gift_given[i] - gift_received[i] for i in range(n)]
    
    # 4. 다음 달에 받을 선물의 수를 저장할 리스트 초기화
    gifts_to_receive = [0] * n
    
    # 모든 친구 쌍을 순회 (중복 비교 방지)
    for i in range(n):
        for j in range(i + 1, n):
            # i와 j를 비교
            gifts_i_to_j = gift_matrix[i][j]
            gifts_j_to_i = gift_matrix[j][i]
            
            if gifts_i_to_j > gifts_j_to_i:
                # i가 j보다 더 많이 준 경우, i는 j로부터 선물을 하나 받음
                gifts_to_receive[i] += 1
            elif gifts_j_to_i > gifts_i_to_j:
                # j가 i보다 더 많이 준 경우, j는 i로부터 선물을 하나 받음
                gifts_to_receive[j] += 1
            else:
                # 선물 주고받은 수가 같거나 기록이 없는 경우
                if gift_index[i] > gift_index[j]:
                    # i의 선물 지수가 j보다 높으면 i는 j로부터 선물을 하나 받음
                    gifts_to_receive[i] += 1
                elif gift_index[j] > gift_index[i]:
                    # j의 선물 지수가 i보다 높으면 j는 i로부터 선물을 하나 받음
                    gifts_to_receive[j] += 1
                # 선물 지수도 같으면 아무도 받지 않음
    
    # 5. 가장 많이 선물을 받은 수를 찾음
    max_gifts = max(gifts_to_receive)
    
    return max_gifts
