from string import ascii_lowercase, ascii_uppercase

opts = ascii_lowercase + ascii_uppercase
ans = 0

lst = []

with open("in.txt", "r") as f:
    for s in f.readlines():
        lst.append(s.strip('\n'))
        n = len(s)
        comp1, comp2 = s[: n // 2], s[n // 2 :]
        for c in comp1:
            if c in comp2:
                priority = opts.index(c) + 1
                ans += priority
                break

print(ans)

cur = 0
ans = 0

for cur in range(0, len(lst), 3):
    g1, g2, g3 = lst[cur], lst[cur + 1], lst[cur + 2]

    for c in g1:
        if c in g2 and c in g3:
            priority = opts.index(c) + 1
            ans += priority
            break

print(ans)
