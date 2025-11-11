import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
p = 'I' + ('OI' * n)
answer = 0
i = 0
oi_count = 0

while i < m-2:
    if s[i:i+3] == "IOI":
        oi_count += 1
        i += 2
        
        if oi_count == n:
            answer += 1
            oi_count -= 1
    else:
        oi_count = 0
        i += 1

print(answer)

"""
해당 문제는 string 비교를 하는 구현 문제
단순히 반복문을 통해 m번 반복해서 s내의 p를 직접 비교해가며 찾아낼 수 있겠지만 N이 1 ≤ N ≤ 1,000,000인 상황에서 Pn만큼 슬라이싱을 하면 시간복잡도는 O(N)이 돼서 결국 반복문 안에서는 O(N^2)의 시간복잡도가 되어 시간 초과가 발생
따라서 반복문 한번의 순회 내에서 결과를 찾아내야 함
한번의 순회 내에서 패턴을 찾아내야 하기에 'IOI'를 기준으로 패턴을 찾아내면 됨
슬라이싱은 3으로 고정이기에 시간복잡도는 O(1).
m를 순회하면서 'IOI'를 찾고 oi_count를 증가시키고 다음에 따라오는 OI를 확인하기 위해 인덱스를 2 증가.
oi_count가 n과 같아지면 answer를 증가시키고 oi_count를 1 감소시킴.
oi_count가 n과 같지 않으면 oi_count를 0으로 초기화하고 인덱스를 1 증가.
이 과정을 m-2까지 반복하면 됨.
"""