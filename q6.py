import copy

f = open ('q6p1.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
ingredients = {}
for line in raw_input:
    name, ings = line.split(':')
    ingredients[name] = [x for x in ings.split(',')]
# Now we start
null_ings = set()
things_to_check = ingredients.pop('NULL')
while len(things_to_check) != 0:
    current_ing = things_to_check.pop()
    if current_ing != 'NULL':
        null_ings.add(current_ing)
    if current_ing in ingredients.keys():
        things_to_check += ingredients.pop(current_ing)
print('Part 1: there are ' + str(len(null_ings)) + ' items that make up NULL.')

f = open ('q6p2.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
ingredients = {}
for line in raw_input:
    name, ings = line.split(':')
    ingredients[name] = [x for x in ings.split(',')]
# Now we start
uses_null = set()
uses_null.add('NULL')
while True:
    uses_null_copy = list(uses_null)
    # First pop all main entries that are things that use null
    for item in list(uses_null):
        if item in ingredients.keys():
            ingredients.pop(item)
    # Now check to see what uses null ingredients
    for ing in uses_null_copy:
        for item in ingredients.keys():
            if ing in ingredients[item]:
                uses_null.add(item)
    if uses_null_copy == list(uses_null):
        break
uses_null.discard('NULL')
print('Part 2: there are ' + str(len(uses_null)) + ' items that use NULL.')

f = open ('q6p3.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
ingredients_raw = {}
null_vers = set()
for line in raw_input:
    name, ings = line.split(':')
    ingredients_raw[name] = [x for x in ings.split(',')]
    raw_ings = [x for x in ings.split(',')]
    for item in raw_ings:
        if 'NULL' in item:
            null_vers.add(item)
single_null = []
for nv in null_vers:
    ingredients = copy.deepcopy(ingredients_raw)
    uses_null = set()
    uses_null.add(nv)
    while True:
        uses_null_copy = list(uses_null)
        # First pop all main entries that are things that use null
        for item in list(uses_null):
            if item in ingredients.keys():
                ingredients.pop(item)
        # Now check to see what uses null ingredients
        for ing in uses_null_copy:
            for item in ingredients.keys():
                if ing in ingredients[item]:
                    uses_null.add(item)
        if uses_null_copy == list(uses_null):
            break
    uses_null.discard(nv)
    single_null += [uses_null]
uses_two = set()
# for x in range(len(single_null)-1):
#     set_a = single_null[x]
#     set_b = single_null[x + 1]
#     result = set_a.intersection(set_b)
#     for item in result:
#         uses_two.add(item)
# Now do the intersections
set_a = single_null[0]
set_b = single_null[1]
for item in list(set_a.intersection(set_b)):
    uses_two.add(item)
set_b = single_null[2]
for item in list(set_a.intersection(set_b)):
    uses_two.add(item)
set_a = single_null[1]
for item in list(set_a.intersection(set_b)):
    uses_two.add(item)

uses_two.discard('NULLv1')
uses_two.discard('NULLv2')
uses_two.discard('NULLv3')
print('Part 3: there are ' + str(len(list(uses_two))) + ' items that use at last two versions of NULL')
