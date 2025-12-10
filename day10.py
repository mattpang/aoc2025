from itertools import combinations, permutations, combinations_with_replacement
from typing import Iterable
from scipy.optimize import linprog

d = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

d = open("inputs/10.txt").read()

data = []
tally = 0
p2_tally = 0
calc_p1 = True
for line in d.splitlines():
    elements = line.split(" ")
    outcome = [i == "#" for i in elements[0][1:-1]]
    voltages = list(map(int, elements[-1][1:-1].split(",")))

    # print(outcome)
    # print(combos)
    # print(voltages)

    combos = list(map(eval, elements[1:-1]))

    smallest_press = 1000000
    if calc_p1:
        for l in range(1, 10):
            for combo in combinations_with_replacement(combos, l):
                state = [False] * len(outcome)
                v = [0] * len(outcome)

                for i, seq in enumerate(combo):
                    if type(seq) is tuple:
                        for s in seq:
                            state[s] = not state[s]
                    else:
                        state[seq] = not state[seq]

                    if state == outcome:
                        if len(combo) < smallest_press:
                            smallest_press = len(combo)
                            # print(combo,len(combo))
                        break

        # print(smallest_press)
        if smallest_press == 1000000:
            print("no lower found for line:", line)
        tally += smallest_press

    # force every entry to be a tuple so we don't fuck up iterators
    combos = [eval(b[:-1] + ",)") for b in elements[1:-1]]
    # part 2 is linear programming.
    switches = [[(i in b) for b in combos] for i in range(len(voltages))]
    p2_tally += int(linprog([1 for b in combos], A_eq=switches, b_eq=voltages, integrality=1).fun)

print(tally)
print(p2_tally)
