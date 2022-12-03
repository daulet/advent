
rename = {
    "X": "A", # rock
    "Y": "B", # paper
    "Z": "C", # scissors
}

order = ["A", "B", "C", "A", "B"]
pos = {
    "A": 3,
    "B": 1,
    "C": 2,
}

cost = {
    "A": 1,
    "B": 2,
    "C": 3,
}

def solve(line):
    a, b = line.split()
    b = rename[b]

    score = cost[b]
    if a == order[pos[b]-1]:
        score += 6
    if a == order[pos[b]+1]:
        score += 0
    if a == order[pos[b]]:
        score += 3

    return score

if __name__ == "__main__":
   with open('adv03.in') as f:
        print(sum(solve(line) for line in f.readlines()))
