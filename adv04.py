
outcome = {
    "X": -1, # lose
    "Y": 0, # draw
    "Z": 1, # win
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

outcome_cost = {
    -1: 0,
    0: 3,
    1: 6,
}

def solve(line):
    a, b = line.split()
    dir = outcome[b]

    play = order[pos[a]+dir]
    return cost[play] + outcome_cost[dir]    

if __name__ == "__main__":
    with open('adv03.in') as f:
        print(sum(solve(line) for line in f.readlines()))
