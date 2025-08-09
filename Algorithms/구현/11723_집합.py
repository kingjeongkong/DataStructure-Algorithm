import sys

n = int(input())
s = set()

for _ in range(n):
    cmd = sys.stdin.readline().split()
    cal = cmd[0]
    num = int(cmd[1]) if len(cmd) > 1 else None
    
    if cal == "add":
        s.add(num)
    elif cal == "remove" and num in s:
        s.remove(num)
    elif cal == "check":
        if num in s:
            print("1")
        else:
            print("0")
    elif cal == "toggle":
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif cal == "all":
        s.update(range(1, 21))
    elif cal == "empty":
        s = set()

"""
이 문제는 단순 구현 문제
하지만 연산의 수 M (1 ≤ M ≤ 3,000,000)로 매우 크고 중복된 수가 들어올 경우 무시 and 빠르게 객체 내에서 수를 찾아야 하므로 set을 사용하는게 관건
"""