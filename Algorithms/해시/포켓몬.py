def solution(nums):
    n = len(nums)
    pokemon_kind = {}

    for pokemon in nums:
        pokemon_kind[pokemon] = pokemon_kind.get(pokemon, 0) + 1

    if len(pokemon_kind) > n / 2:
        return n / 2
    else :
        return len(pokemon_kind)
    


def solution(nums):
    return min(len(set(nums)), len(nums)//2)

    
"""
해시를 사용해야 하는 상황

1.1 중복을 확인해야 할 때
- 리스트나 배열에서 중복된 값이 있는지 확인하거나, 중복된 값을 제거해야 할 때.
- 해시의 특징: 딕셔너리나 set은 중복을 허용하지 않으므로, 삽입과 동시에 중복 여부를 확인할 수 있습니다.

1.2 특정 값의 존재 여부를 빠르게 확인해야 할 때
- 리스트에서 특정 값이 존재하는지 확인하는 연산은 O(n)(선형 탐색)이지만, 해시는 O(1)(평균)로 확인 가능합니다.

1.3 데이터 매핑(키-값 쌍)이 필요한 경우
- 데이터를 키-값 쌍으로 저장하고 빠르게 조회해야 할 때.
"""

# 해당 문제는 선택할 수 있는 최대의 포켓몬 종류 수를 구해야 함
# 중복이 가능한 종류 수이므로 dictionary나 set를 이용해서 풀 수 있음.