
from itertools import combinations

d = """987654321111111
811111111111119
234234234234278
818181911112111
"""

d = open('inputs/3.txt').read()

grid= []
for line in d.splitlines():
    row = [] 
    for x in line:
        row.append(int(x))
    grid.append(row)
# print(grid)

ans = 0 
for row in grid:
    m = 0
    for i,x in enumerate(row):
        if i==len(row)-1:
            break
        tmp = int(str(x)+str(max(row[i+1:])))
        if tmp>m:
            m=tmp
    # print(m)
    ans+=m
print(ans)



# part 2. whatever left to right combo of 12 on is largest. 
# this works for smaller case, but we will run out of ram since 100! is too large
# print(sum([max([int(''.join(x)) for x in list(combinations(g,12))]) for g in grid]))

# what's the biggest in the first :-11 digits. etc etc. then note down pos. repeat. 

def maxj(row, n):
    if n == 1:
        return max(row)
    x = max(row[: -(n - 1)])
    i = row.index(x)
    return x + maxj(row[i + 1 :], n - 1)

tot = 0
for row in d.splitlines():
    tot+=int(maxj(row,12))

print(tot)
    