d = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
d = open('inputs/2.txt').read()

ans = 1227775554

def check_vals(x):

    combo = str(x)
    h1,h2 = combo[0:len(combo)//2] , combo[len(combo)//2:]
    if h1 == h2:
        return True
    else:
        return False

def check_any_pos(x):
    combo = str(x)
    # if the string is made of only these substr
    for c in range(1,len(combo)):
        if combo.replace(combo[0:c],'').__len__() == 0:
            return True
    return False


assert check_vals(1188511885) == True

total = 0
for a,b in map(lambda x:x.split('-'), d.split(',')):
    for x in range(int(a),int(b)+1):
        if check_vals(x):
            total+=x
print(total)

assert check_any_pos(2121212121) == True
assert check_any_pos(824824824) == True

total = 0
for a,b in map(lambda x:x.split('-'), d.split(',')):
    # print(a,b)
    for x in range(int(a),int(b)+1):
        if check_vals(x) or check_any_pos(x):
            total+=x
print(total)