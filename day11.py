from functools import cache

d = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

d = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

d = open("inputs/11.txt").read()


nodes = {}
for source, targets in map(lambda x: x.split(":"), d.splitlines()):
    s = source.strip()
    t = list(map(lambda x: x.strip(), targets.strip().split(" ")))

    nodes[s] = t

nodes["out"] = []


@cache
def paths(source, target, dac, fft):
    if source == "fft":
        fft = True

    if source == "dac":
        dac = True

    if source == target:
        return 1 if dac and fft else 0

    return sum(paths(node, target, dac, fft) for node in nodes[source])


print(paths("you", "out", True, True))
print(paths("svr", "out", False, False))
