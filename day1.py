mock = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

# mock = """R1000
# """

d = open('inputs/1.txt').read().splitlines()
# d = mock.splitlines()
# print(d)
count = 0 
pos = 50
for x in d:
    if x.startswith('L'):
        pos-= int(x[1:])
    elif x.startswith('R'):
        pos+= int(x[1:])
    pos = pos % 100
    if pos==0:
        count+=1
    # print(pos)
print(count)

# part 2 any click crossing zero. 
count = 0 
p = 50

def make_move(pos,dir,size):
    cs=0
    for i in range(size):
        pos = pos + dir 
        pos = pos %100
        if pos == 0:
            cs+=1

    return cs,pos

for x in d:
    move = int(x[1:])
    if x.startswith('L'):
        c,p = make_move(p,-1,move)
    elif x.startswith('R'):
        c,p = make_move(p,1,move)

    count+=c
    # if p==0:
    #     count+=1


print(count)
