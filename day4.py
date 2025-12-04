# less than 4
d = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

d = open('inputs/4.txt').read()
# add padding all around the grid
grid = [[x for x in '.'+y+'.'] for y in d.splitlines() ]

width = len(grid[0])
height = len(grid)
grid.insert(0,['.']*width)
grid.append(['.']*width)

# print(grid)

pick = 0
ansmap = []
for y,row in enumerate(grid):
    ansrow=''
    for x,c in enumerate(row):
        tally=0
        
        options = [(-1,0),(-1,-1),(-1,1),(1,0),(1,-1),(1,1),(0,1),(0,-1)]
        assert len(set(options)) == 8

        for i,j in options:
            try:
                if grid[(y+j)][(x+i)]=='@':
                    tally+=1
            except IndexError:
                pass

        if tally<4 and grid[y][x]=='@':
            pick+=1
            ansrow+='X'
        else:
            ansrow+=grid[y][x]
    ansmap.append(ansrow)
print(pick)

# part 2. do it until it can't reduce any more
start_val = 0 

while True:
    now_val = start_val
    for y,row in enumerate(grid):
        ansrow=''
        for x,c in enumerate(row):
            tally=0
            
            options = [(-1,0),(-1,-1),(-1,1),(1,0),(1,-1),(1,1),(0,1),(0,-1)]
            assert len(set(options)) == 8

            for i,j in options:
                try:
                    if grid[(y+j)][(x+i)]=='@':
                        tally+=1
                except IndexError:
                    pass

            if tally<4 and grid[y][x]=='@':
                now_val+=1
                grid[y][x]='.'

        ansmap.append(ansrow)

    if start_val == now_val:
        break
    start_val = now_val

print(now_val)