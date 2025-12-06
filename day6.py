from collections import defaultdict,Counter
from operator import add, mul

d = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""
d = open('./inputs/6.txt').read()

columns = defaultdict(list)
operator = dict()

for line in d.splitlines()[:-1]:

    col_id = 0
    for c in line.split(" "):
        if c.isdigit() and not c.isspace():
            columns[col_id].append(int(c))
            col_id += 1

rows = d.splitlines()

col_id = 0
for ops in d.splitlines()[-1]:

    for c in ops.split(" "):
        if c =='+' or c=='*':
            operator[col_id] = c
            col_id += 1



total = 0 
for i in columns.keys():
    if operator[i] == "+":
        sub_total=0
        for v in columns[i]:

            sub_total += v
    elif operator[i] == "*":
        sub_total=1
        for v in columns[i]:

            sub_total *= v

    total+=sub_total

print(total)

# part 2
# fuck its the inputs's position. not what I've done to pre process it. the alignment is from the op source.

grid = defaultdict(list)
this_op = d.splitlines()[-1][0]

current_op = dict()
tally = len(d.splitlines())-1
space_count = Counter()

for line in d.splitlines()[:-1]:
    for i,c in enumerate(line):
        if c.isdigit():
            grid[i].append(c)
        elif c==' ':
            space_count[i]+=1


for i,c in enumerate(d.splitlines()[-1]):
    if c=='+' or c=='*':
        current_op[i] = c

total = 0
if current_op[0]=='*':
    sub_total = 1
else:
    sub_total = 0
this_op = current_op[0]
for i in range(0,len(d.splitlines()[0])):
    if current_op.get(i):
        this_op= current_op.get(i)

    if space_count[i]==tally:
        total+=sub_total
        if current_op[i+1]=='*':
            sub_total=1
        else:
            sub_total=0
    if this_op=='*':
        if len(grid[i])>0:
            sub_total*= int(''.join(grid[i]))
    else:
        if len(grid[i])>0:
            sub_total+= int(''.join(grid[i]))
    

total+=sub_total

print(total)