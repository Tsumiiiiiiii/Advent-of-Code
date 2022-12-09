
ans = 0

decode = {
    'A' : 'R',
    'X' : 'R',
    'B' : 'P',
    'Y' : 'P',
    'C' : 'S',
    'Z' : 'S' 
}

score = {
    'R' : 1,
    'P' : 2,
    'S' : 3
}

win = ['RP', 'SR', 'PS']

with open("in.txt", "r") as f:
    for s in f.readlines():
        s = s.strip('\n')
        
        seq = decode[s[0]] + decode[s[2]]
        
        points = score[seq[1]]
        if seq in win:
            points += 6
        elif seq[0] == seq[1]:
            points += 3
        else:
            points += 0
    
        ans += points

print(ans)

winning = {
    'R' : 'P',
    'P' : 'S',
    'S' : 'R',
}

losing = {
    'P' : 'R',
    'S' : 'P',
    'R' : 'S'
}

ans = 0

with open("in.txt", "r") as f:
    for s in f.readlines():
        s = s.strip('\n')
        move = decode[s[0]]

        if s[2] == 'X':
            points = 0 + score[losing[move]]
        elif s[2] == 'Y':
            points = 3 + score[move]
        else:
            points = 6 + score[winning[move]]
    
        ans += points


print(ans)
