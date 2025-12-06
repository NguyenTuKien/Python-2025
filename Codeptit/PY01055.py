for _ in range(int(input())):
    n = input().strip()
    ok = False
    if len(n) % 2 == 0 or n[0] == n[1]:
        print("NO")
        ok = True
        continue
    for i in range(0, len(n), 2):
        if n[i] != n[0]:
            print("NO")
            ok = True
            break
    if not ok:
        print("YES")