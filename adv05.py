

def priority(c):
    if 'a' <= c <= 'z':
        return ord(c)-ord('a')+1
    if 'A' <= c <= 'Z':
        return ord(c)-ord('A')+27

def solve(line):
    a, b = line[:len(line)//2], line[len(line)//2:]
    vals = set(a)
    for c in b:
        if c in vals:
            return priority(c)


if __name__ == "__main__":
    with open('adv05.in') as f:
        print(sum(solve(line) for line in f.readlines()))
