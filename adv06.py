def priority(c):
    if 'a' <= c <= 'z':
        return ord(c)-ord('a')+1
    if 'A' <= c <= 'Z':
        return ord(c)-ord('A')+27

def solve(l1, l2, l3):
    s = set(l1).intersection(set(l2)).intersection(set(l3))
    if '\n' in s:
        s.remove('\n')
    return min(priority(c) for c in s)


if __name__ == "__main__":
    with open('adv05.in') as f:
        lines = f.readlines()
        sum = 0
        for i in range(0, len(lines), 3):
            sum += solve(lines[i], lines[i+1], lines[i+2])
        print(sum)