with open("in.txt", 'r') as f:
    signal = f.read().strip()

ans = 0

for i in range(len(signal)):
    st = set()
    for c in signal[i : i + 14]:
        st.add(c)
    if len(st) == 14:
        ans = i + 14
        break

print(ans)
