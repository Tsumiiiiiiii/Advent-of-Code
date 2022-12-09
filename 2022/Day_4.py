
ans = 0

with open("in.txt", "r") as f:
    for s in f.readlines():
        s = s.strip()

        a, b = s.split(',')
        st1, ed1 = map(int, a.split('-'))
        st2, ed2 = map(int, b.split('-'))

        if (st1 <= st2 and ed1 >= ed2) or (st2 <= st1 and ed2 >= ed1):
            ans += 1

print(ans)

ans = 0

with open("in.txt", "r") as f:
    for s in f.readlines():
        s = s.strip()
        
        a, b = s.split(',')
        st1, ed1 = map(int, a.split('-'))
        st2, ed2 = map(int, b.split('-'))

        if st2 > ed1 or st1 > ed2:
            continue
        
        ans += 1

print(ans)
