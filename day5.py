d = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

d = open('inputs/5.txt').read()

item=False
x=[]
r = [] 
for row in d.splitlines():
    if row=='':
        item = True
        continue

    if item:
        x.append(int(row))
    else:
        a,b = row.split('-')
        r.append((int(a),int(b)))

# print(r)
# print(x)

flags =set()
total=0
for i in x:
    for a,b in r:
        if i>=a and i<=b:
            total+=1
            flags.add(i)

print(len(flags))

# how much do things over lap. and if they do
# need the left edge to move to the larger of the next
count = 0
n = 0
for a, b in sorted(r):
    new_n = max(n, b)
    if a <= n:
        count += new_n - n
    else:
        count += b - a + 1
    n = new_n

print(count)