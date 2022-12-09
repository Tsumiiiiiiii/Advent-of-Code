
ommit = [9, 10]

cur_line = 0
n = 9

stk = [[] for _ in range(n)]

def make_stack(inp):
    stk_id = 0
    spc = 0

    for c in inp:
        if not c:
            spc += 1
            if spc == 4:
                stk_id += 1
                spc = 0
        else:
            stk[stk_id].append(c[1])
            spc = 0
            stk_id += 1
        
        


def process_change(inp):
    cnt, fr, to = int(inp[1]), int(inp[3]), int(inp[5])
    cnt, fr, to = cnt - 1, fr - 1, to - 1
    to_move = stk[fr][:cnt + 1]
    stk[to] = to_move + stk[to]
    stk[fr] = stk[fr][cnt + 1:]


with open("in.txt", "r") as f:
    for s in f.readlines():
        cur_line += 1
        if cur_line in ommit:
            continue
        s = s.strip('\n').split(' ')

        if cur_line < 9:
            make_stack(s)
        else:
            process_change(s)


ans = ""

for st in stk:
    ans += st[0]

print(ans)
