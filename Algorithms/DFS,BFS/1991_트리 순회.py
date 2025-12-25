import sys

n = int(sys.stdin.readline())
tree = {}
for _ in range(n):
    p, c1, c2 = sys.stdin.readline().strip().split()
    tree[p] = [c1, c2]
pre = []
ino = []
pos = []

def preorder(node):
    if node == '.':
        return
    pre.append(node)
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    ino.append(node)
    inorder(tree[node][1])
    
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    pos.append(node)

preorder('A')
inorder('A')
postorder('A')
print(''.join(pre))
print(''.join(ino))
print(''.join(pos))

"""
해당 문제는 트리 순회 문제.
부모 노드, 자식 노드의 관계가 명확하므로 딕셔너리를 통해서 트리를 저장함
트리 순회는 DFS를 통해서 진행
전위, 중위, 후위 각각 진행해줌
"""