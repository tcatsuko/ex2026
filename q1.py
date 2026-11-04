f = open('q1p1.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
outposts = [int(x) for x in raw_input[0].split(',')]
cones = 0
for outpost in outposts:
    for x in range(1,outpost + 1):
        if x * x == outpost:
            break
        if x * x > outpost:
            needed = (x*x) - outpost
            cones += needed
            break
print('Part 1: You need ' + str(cones) + ' cones.')

f = open('q1p2.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
outposts = [int(x) for x in raw_input[0].split(',')]
cones = 0
for outpost in outposts:
    for x in range(3, max(outposts)):
        needed = (x * 4) - 4
        if outpost == needed:
            break
        if needed > outpost:
            cones += (needed - outpost)
            break
print('Part 2: you need ' + str(cones) + ' cones.')

f = open('q1p3.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
outposts = [int(x) for x in raw_input[0].split(',')]
cones = 0
for outpost in outposts:
    for x in range(3, max(outposts) + 2, 2):
        needed = (x * x) - 1
        if needed == outpost:
            break
        if needed > outpost:
            cones += (needed - outpost)
            break
print('Part 3: you need ' + str(cones) + ' cones.')

            