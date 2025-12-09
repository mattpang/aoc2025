from itertools import combinations

d = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

d= open('inputs/9.txt').read()

pos = []
for line in d.split():
    x,y = map(int,line.split(','))
    pos.append((x,y))


largest = 0
for a,b in combinations(pos,2):
    area = (abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1)

    if area>largest:
        largest=area

print(largest)
# store the outlines of this shape, until next point. so when we make area, we check all edges are allowed in an enclosed area.
# maybe use a libary? Do it with shapely
from shapely import Polygon
shape = Polygon(pos)
largest = 0
for a,b in combinations(pos,2):
    box = Polygon([(a[0],a[1]),(a[0],b[1]),(b[0],b[1]),(b[0],a[1])])
    if box.area>largest and shape.contains(box):
        largest=box.area
        x,y = a,b

# because area you count inclusive of edges
print((abs(x[0]-y[0])+1)*(abs(x[1]-y[1])+1))

