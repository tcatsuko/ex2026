f = open('q5p1.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
user_map = []
for line in raw_input:
    user_map += [[x for x in line]]
# Determine the center
y_center = len(user_map) // 2
x_center = len(user_map[0]) // 2
user_map[y_center][x_center] = '#'
points_to_check = set()

# Now buffer the map
width = len(user_map[0])
height = len(user_map)
new_map = []
new_map += [['0'] * (width + 2)]
for item in user_map:
    new_map += [['0'] + item + ['0']]
new_map += [['0'] * (width + 2)]
user_map = new_map
x_center += 1
y_center += 1
points_to_check.add((x_center - 1, y_center - 1))
points_to_check.add((x_center, y_center - 1))
points_to_check.add((x_center + 1, y_center - 1))
points_to_check.add((x_center - 1, y_center ))
points_to_check.add((x_center + 1, y_center))
points_to_check.add((x_center - 1, y_center + 1))
points_to_check.add((x_center, y_center + 1))
points_to_check.add((x_center + 1, y_center + 1))


# We are buffered, now start to run through this all
while len(points_to_check) != 0:
    # First, create a copy of the map so we don't start to get some false positives
    new_map = []
    for line in user_map:
        new_map += [line[:]]
    current_round = list(points_to_check)
    points_to_check = set()
    for point in current_round:
        x, y = point
        if x == 0:
            continue
        elif x == len(user_map[0]) - 1:
            continue
        elif y == 0:
            continue
        elif y == len(user_map) - 1:
            continue

        lands = 0
        if user_map[y-1][x-1] == '1' or user_map[y-1][x-1] == '#':
            lands += 1
        if user_map[y - 1][x] == '1' or user_map[y - 1][x] == '#':
            lands += 1
        if user_map[y - 1][x + 1] == '1' or user_map[y - 1][x + 1] == '#':
            lands += 1
        if user_map[y][x - 1] == '1' or user_map[y][x - 1] == '#':
            lands += 1
        if user_map[y][x + 1] == '1' or user_map[y][x + 1] == '#':
            lands += 1
        if user_map[y + 1][x - 1] == '1' or user_map[y + 1][x - 1] == '#':
            lands += 1
        if user_map[y + 1][x] == '1' or user_map[y + 1][x] == '#':
            lands += 1
        if user_map[y + 1][x + 1] == '1' or user_map[y + 1][x + 1] == '#':
            lands += 1
        if lands >= 5:
            new_map[y][x] = '#'
            # Fill in some new points to check
            points_to_check.add((x-1, y-1))
            points_to_check.add((x, y-1))
            points_to_check.add((x+1, y-1))
            points_to_check.add((x-1, y))
            points_to_check.add((x+1,y))
            points_to_check.add((x-1,y+1))
            points_to_check.add((x, y+1))
            points_to_check.add((x+1, y+1))
    if user_map == new_map:
        user_map = new_map
        break
    user_map = new_map
land_cells = 0
for line in user_map:
    land_cells += line.count('#')
print('Part 1: there are ' + str(land_cells) + ' land cells.')

############. Part 2

f = open('q5p2.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
user_map = []
for line in raw_input:
    user_map += [[x for x in line]]
# Determine the center
y_center = len(user_map) // 2
x_center = len(user_map[0]) // 2
user_map[y_center][x_center] = '#'
points_to_check = set()

# Now buffer the map
width = len(user_map[0])
height = len(user_map)
new_map = []
new_map += [['0'] * (width + 2)]
for item in user_map:
    new_map += [['0'] + item + ['0']]
new_map += [['0'] * (width + 2)]
user_map = new_map
x_center += 1
y_center += 1
points_to_check.add((x_center - 1, y_center - 1))
points_to_check.add((x_center, y_center - 1))
points_to_check.add((x_center + 1, y_center - 1))
points_to_check.add((x_center - 1, y_center ))
points_to_check.add((x_center + 1, y_center))
points_to_check.add((x_center - 1, y_center + 1))
points_to_check.add((x_center, y_center + 1))
points_to_check.add((x_center + 1, y_center + 1))


# We are buffered, now start to run through this all
while len(points_to_check) != 0:
    # First, create a copy of the map so we don't start to get some false positives
    new_map = []
    for line in user_map:
        new_map += [line[:]]
    current_round = list(points_to_check)
    points_to_check = set()
    for point in current_round:
        x, y = point
        if x == 0:
            continue
        elif x == len(user_map[0]) - 1:
            continue
        elif y == 0:
            continue
        elif y == len(user_map) - 1:
            continue

        lands = 0
        if user_map[y-1][x-1] == '1' or user_map[y-1][x-1] == '#':
            lands += 1
        if user_map[y - 1][x] == '1' or user_map[y - 1][x] == '#':
            lands += 1
        if user_map[y - 1][x + 1] == '1' or user_map[y - 1][x + 1] == '#':
            lands += 1
        if user_map[y][x - 1] == '1' or user_map[y][x - 1] == '#':
            lands += 1
        if user_map[y][x + 1] == '1' or user_map[y][x + 1] == '#':
            lands += 1
        if user_map[y + 1][x - 1] == '1' or user_map[y + 1][x - 1] == '#':
            lands += 1
        if user_map[y + 1][x] == '1' or user_map[y + 1][x] == '#':
            lands += 1
        if user_map[y + 1][x + 1] == '1' or user_map[y + 1][x + 1] == '#':
            lands += 1
        if lands >= 5:
            new_map[y][x] = '#'
            # Fill in some new points to check
            points_to_check.add((x-1, y-1))
            points_to_check.add((x, y-1))
            points_to_check.add((x+1, y-1))
            points_to_check.add((x-1, y))
            points_to_check.add((x+1,y))
            points_to_check.add((x-1,y+1))
            points_to_check.add((x, y+1))
            points_to_check.add((x+1, y+1))
    if user_map == new_map:
        user_map = new_map
        break
    user_map = new_map
# Now start to convert to sand
# Start by changing 1 and 0 to .
for line in user_map:
    line[:] = ['.' if x == '0' else x for x in line]
    line[:] = ['.' if x == '1' else x for x in line]
# Next, get the border set
def count_neighbors(user_map, x, y, marker):
    count = 0
    if user_map[y-1][x-1] == marker:
        count += 1
    if user_map[y-1][x] == marker:
        count += 1
    if user_map[y-1][x+1] == marker:
        count += 1
    if user_map[y][x-1] == marker:
        count += 1
    if user_map[y][x+1] == marker:
        count += 1
    if user_map[y+1][x-1] == marker:
        count += 1
    if user_map[y+1][x] == marker:
        count += 1
    if user_map[y+1][x+1] == marker:
        count += 1
    return count

for y in range(1, len(user_map) - 1):
    for x in range(1, len(user_map[0]) - 1):
        if user_map[y][x] == '#':
            near_water = count_neighbors(user_map, x, y, '.')
            if near_water > 0:
                user_map[y][x] = '='
while True:
    new_map = []
    for line in user_map:
        new_map += [line[:]]
    for y, line in enumerate(user_map):
        if y == 0:
            continue
        if y == len(user_map) - 1:
            continue
        for x in range(1, len(line) - 1):
            if user_map[y][x] == '#':
                sand_count = count_neighbors(user_map, x, y, '=')
                if sand_count >= 5:
                    new_map[y][x] = '='
    if new_map == user_map:
        break
    user_map = new_map

sand_cells = 0
for line in user_map:
    sand_cells += line.count('=')
print('Part 2: there are ' + str(sand_cells) + ' sand cells.')

######### Part 3
############. Part 2

f = open('q5p3.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
user_map = []
for line in raw_input:
    user_map += [[x for x in line]]
# Determine the center
y_center = len(user_map) // 2
x_center = len(user_map[0]) // 2
user_map[y_center][x_center] = '#'
points_to_check = set()

# Now buffer the map
width = len(user_map[0])
height = len(user_map)
new_map = []
new_map += [['0'] * (width + 2)]
for item in user_map:
    new_map += [['0'] + item + ['0']]
new_map += [['0'] * (width + 2)]
user_map = new_map
x_center += 1
y_center += 1
points_to_check.add((x_center - 1, y_center - 1))
points_to_check.add((x_center, y_center - 1))
points_to_check.add((x_center + 1, y_center - 1))
points_to_check.add((x_center - 1, y_center ))
points_to_check.add((x_center + 1, y_center))
points_to_check.add((x_center - 1, y_center + 1))
points_to_check.add((x_center, y_center + 1))
points_to_check.add((x_center + 1, y_center + 1))


# We are buffered, now start to run through this all
while len(points_to_check) != 0:
    # First, create a copy of the map so we don't start to get some false positives
    new_map = []
    for line in user_map:
        new_map += [line[:]]
    current_round = list(points_to_check)
    points_to_check = set()
    for point in current_round:
        x, y = point
        if x == 0:
            continue
        elif x == len(user_map[0]) - 1:
            continue
        elif y == 0:
            continue
        elif y == len(user_map) - 1:
            continue

        lands = 0
        if user_map[y-1][x-1] == '1' or user_map[y-1][x-1] == '#':
            lands += 1
        if user_map[y - 1][x] == '1' or user_map[y - 1][x] == '#':
            lands += 1
        if user_map[y - 1][x + 1] == '1' or user_map[y - 1][x + 1] == '#':
            lands += 1
        if user_map[y][x - 1] == '1' or user_map[y][x - 1] == '#':
            lands += 1
        if user_map[y][x + 1] == '1' or user_map[y][x + 1] == '#':
            lands += 1
        if user_map[y + 1][x - 1] == '1' or user_map[y + 1][x - 1] == '#':
            lands += 1
        if user_map[y + 1][x] == '1' or user_map[y + 1][x] == '#':
            lands += 1
        if user_map[y + 1][x + 1] == '1' or user_map[y + 1][x + 1] == '#':
            lands += 1
        if lands >= 5:
            new_map[y][x] = '#'
            # Fill in some new points to check
            points_to_check.add((x-1, y-1))
            points_to_check.add((x, y-1))
            points_to_check.add((x+1, y-1))
            points_to_check.add((x-1, y))
            points_to_check.add((x+1,y))
            points_to_check.add((x-1,y+1))
            points_to_check.add((x, y+1))
            points_to_check.add((x+1, y+1))
    if user_map == new_map:
        user_map = new_map
        break
    user_map = new_map
# Now start to convert to sand
# Start by changing 1 and 0 to .
for line in user_map:
    line[:] = ['.' if x == '0' else x for x in line]
    line[:] = ['.' if x == '1' else x for x in line]
# Next, get the border set

for y in range(1, len(user_map) - 1):
    for x in range(1, len(user_map[0]) - 1):
        if user_map[y][x] == '#':
            near_water = count_neighbors(user_map, x, y, '.')
            if near_water > 0:
                user_map[y][x] = '='
while True:
    new_map = []
    for line in user_map:
        new_map += [line[:]]
    for y, line in enumerate(user_map):
        if y == 0:
            continue
        if y == len(user_map) - 1:
            continue
        for x in range(1, len(line) - 1):
            if user_map[y][x] == '#':
                sand_count = count_neighbors(user_map, x, y, '=')
                if sand_count >= 5:
                    new_map[y][x] = '='
    if new_map == user_map:
        break
    user_map = new_map
# First pass for trees
new_map = []
for line in user_map:
    new_map += [line[:]]
for y in range(2, len(user_map) - 4):
    for x in range(2, len(user_map[0])-4):
        # Check around to see if land fits
        land_count = 0
        if user_map[y-2][x-1] == '#':
            land_count += 1
        if user_map[y-2][x] == '#':
            land_count += 1
        if user_map[y-2][x+1] == '#':
            land_count += 1
        if user_map[y-1][x-2] == '#':
            land_count += 1
        if user_map[y-1][x-1] == '#':
            land_count += 1
        if user_map[y-1][x] == '#':
            land_count += 1
        if user_map[y-1][x+1] == '#':
            land_count += 1
        if user_map[y-1][x+2] == '#':
            land_count += 1
        if user_map[y][x-2] == '#':
            land_count += 1
        if user_map[y][x-1] == '#':
            land_count += 1
        if user_map[y][x+1] == '#':
            land_count += 1
        if user_map[y][x+2] == '#':
            land_count += 1
        if user_map[y+1][x-2] == '#':
            land_count += 1
        if user_map[y+1][x-1] == '#':
            land_count += 1
        if user_map[y+1][x] == '#':
            land_count += 1
        if user_map[y+1][x+1] == '#':
            land_count += 1
        if user_map[y+1][x+2] == '#':
            land_count += 1
        if user_map[y+2][x-1] == '#':
            land_count += 1
        if user_map[y+2][x] == '#':
            land_count += 1
        if user_map[y+2][x+1] == '#':
            land_count += 1
        if land_count == 20:
            new_map[y][x] = '@'
user_map = new_map
for step in range(2):
    new_map = []
    for line in user_map:
        new_map += [line[:]]
    for y, line in enumerate(user_map):
        if y == 0:
            continue
        if y == len(user_map) - 1:
            continue
        for x in range(1, len(line) - 1):
            if user_map[y][x] == '#':
                sand_count = count_neighbors(user_map, x, y, '=')
                tree_count = count_neighbors(user_map, x, y, '@')
                if ((sand_count == 0) and (tree_count >= 4)):
                    new_map[y][x] = '@'
    user_map = new_map

tree_cells = 0
for line in user_map:
    tree_cells += line.count('@')
print('Part 3: there are ' + str(tree_cells) + ' tree cells.')