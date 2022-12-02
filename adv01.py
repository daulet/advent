
def solve(lines):
    cur, max = 0, 0
    for line in lines:
        if line[0] == '\n':
            cur = 0
            continue
        cur += int(line)
        if cur > max:
            max = cur

    return max
        
if __name__ == '__main__':
    with open('adv01.in') as f:
        lines = f.readlines()
    ans = solve(lines)
    print(ans)
    