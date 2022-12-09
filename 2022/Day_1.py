w = []
ans = 0

with open("in.txt", "r") as f:
    w = f.read().split('\n')

w.append('')

cur = 0
lst = []

for x in w:
    if x == '':
        ans = max(ans, cur)
        lst.append(cur)
        cur = 0
    else:
        cur += int(x)
lst = sorted(lst, reverse=True)
print(ans)
print(sum(lst[0:3]))
