def get_pos(k, a, m):
    floor_global = (k - 1) // a
    entrance = floor_global // m + 1
    floor = floor_global % m + 1
    return entrance, floor


K1, M, K2, P2, N2 = map(int, input().split())

possible_p = set()
possible_n = set()

for a in range(1, 10**6 + 1):  # a = квартир на этаже
    p2, n2 = get_pos(K2, a, M)

    if p2 == P2 and n2 == N2:
        p1, n1 = get_pos(K1, a, M)
        possible_p.add(p1)
        possible_n.add(n1)

if not possible_p:
    print(-1, -1)
else:
    ans_p = possible_p.pop() if len(possible_p) == 1 else 0
    ans_n = possible_n.pop() if len(possible_n) == 1 else 0
    print(ans_p, ans_n)
