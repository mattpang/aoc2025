d = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

d=open('./inputs/7.txt','r').read()

beam = dict()
split = 0 
grid = []
combos = set()
# xth row
# ith column coords , could have gone left or right. 
from collections import defaultdict
queues = defaultdict(int)
print(queues, queues.get(5))
for x,line in enumerate(d.splitlines()):
    l=""
    nbeam = beam.copy()
    nq = queues.copy()
    for i,c in enumerate(line):
        if c=='S':
            nbeam[i]=1
            nq[i] =1

        if c=='^' and beam.get(i):
            nbeam[i-1]=True
            nbeam[i+1]=True
            split+=1

            nq[i-1] += nq[i]
            nq[i+1] += nq[i]

            del nbeam[i]
            del nq[i]

    grid.append(l)
    queues = nq.copy()
    beam = nbeam.copy()

print(split)
print(sum(queues.values()))
