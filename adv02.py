
def solve(lines):
    a, cur = [], 0
    for line in lines:
        if line[0] == '\n':
            a.append(cur)
            cur = 0
            continue
        cur += int(line)
    a.append(cur)

    a = sorted(a)
    return sum(a[-3:])
        
if __name__ == '__main__':
    with open('adv01.in') as f:
        lines = f.readlines()
    ans = solve(lines)
    print(ans)
    