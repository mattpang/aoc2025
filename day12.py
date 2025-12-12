d = open('inputs/12.txt').read()
ans = d.split('\n\n')    
shape_area = [x.count('#') for x in ans[0:6]]
tiles = [[tuple(map(int,x.split(': ')[0].split('x'))),list(map(int,x.split(': ')[1].split(' ')))] for x in ans[6][:-1].split('\n')]
t=0
for (x,y),counts in tiles:
    total_area = sum([shape_area[i]*c for i,c in enumerate(counts)])
    if (x*y > total_area):
        t+=1
    
print(t)
