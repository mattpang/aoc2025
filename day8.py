import math
import collections

d = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

d = open("./inputs/8.txt", "r").read()


boxes = []
for line in d.splitlines():
    x, y, z = map(int, line.split(","))
    boxes.append((x, y, z))


def distance(x, y):
    return ((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2 + (y[2] - x[2]) ** 2) ** 0.5


# need the closest boxes to eachother
# so precalc the matrix first?
dist = dict()
for b in boxes:
    for bp in boxes:
        if b != bp:
            pair = [b, bp]
            pair = tuple(sorted(pair))
            if pair not in dist:
                dist[pair] = distance(pair[0], pair[1])


dists = sorted(dist.items(), key=lambda x: x[1])

circuits = list(range(len(boxes)))
matched = set()
limit = 1000

def connect(circuits, a: tuple[int], b: tuple[int]):
    circuit1 = circuits[a]
    circuit2 = circuits[b]
    if circuit1 == circuit2:
        return
    for i, circuit in enumerate(circuits):
        if circuit == circuit2:
            circuits[i] = circuit1


for i, ((x, y), r) in enumerate(dists):
    id1 = boxes.index(x)
    id2 = boxes.index(y)
    connect(circuits, id1, id2)

    if i == limit - 1:
        circuits_counted = collections.Counter(circuits)
        largest_circuits = circuits_counted.most_common(3)
        ans = math.prod(count for _, count in largest_circuits)
        print(ans)

    if len(set(circuits)) == 1:
        break

print(x[0] * y[0])
