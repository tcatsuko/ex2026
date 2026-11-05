f = open('q4p1.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
participants = []
# First get a list of all of the ids
idnums = set()
for line in raw_input:
    [id, quest, part, time] = line.split(' ')
    id = int(id.split('=')[1])
    idnums.add(id)
idnums = list(idnums)
for id in idnums:
    participant = {}
    participant['id'] = id
    participant['total_time'] = 0
    participants += [participant]
for line in raw_input:
    [id, quest, part, time] = line.split(' ')
    id = int(id.split('=')[1])
    quest = int(quest.split('=')[1])
    part = int(part.split('=')[1])
    time = int(time.split('=')[1])
    # Get the correct participant from the list, add the time
    for participant in participants:
        if participant['id'] == id:
            participant['total_time'] += time
# Sort the dictionary
participants = sorted(participants, key=lambda x: x['total_time'])
# calculate checksum
checksum = 0
for x, participant in enumerate(participants):
    checksum += (x + 1)*participant['total_time']


print('Part 1: checksum = ' + str(checksum))

f = open('q4p2.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
participants = []
# First get a list of all of the ids
idnums = set()
for line in raw_input:
    [id, quest, part, time] = line.split(' ')
    id = int(id.split('=')[1])
    idnums.add(id)
idnums = list(idnums)
for id in idnums:
    participant = {}
    participant['id'] = id
    participant['total_time'] = 0
    participant['parts'] = 0
    participants += [participant]
for line in raw_input:
    [id, quest, part, time] = line.split(' ')
    id = int(id.split('=')[1])
    quest = int(quest.split('=')[1])
    part = int(part.split('=')[1])
    time = int(time.split('=')[1])
    # Get the correct participant from the list, add the time
    for participant in participants:
        if participant['id'] == id:
            participant['total_time'] += time
            participant['parts'] += 1
# Sort the dictionary
participants = sorted(participants, key=lambda x: (-x['parts'], x['total_time']))
# calculate checksum
checksum = 0
for x, participant in enumerate(participants):
    checksum += (x + 1)*participant['total_time']


print('Part 2: checksum = ' + str(checksum))

f = open('q4p3.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
participants = []
# First get a list of all of the ids
idnums = set()
quests = set()
for line in raw_input:
    [id, quest, part, time] = line.split(' ')
    id = int(id.split('=')[1])
    quest = int(quest.split('=')[1])
    quests.add(quest)
    idnums.add(id)
idnums = list(idnums)
for id in idnums:
    participant = {}
    participant['id'] = id
    participant['total_time'] = 0
    participant['quests'] = []
    participant['score'] = 0
    participants += [participant]
quests = list(quests)
quests.sort()

for line in raw_input:
    [id, quest, part, time] = line.split(' ')
    id = int(id.split('=')[1])
    quest = int(quest.split('=')[1])
    part = int(part.split('=')[1])
    time = int(time.split('=')[1])
    # Get the correct participant from the list, add the time
    for participant in participants:
        if participant['id'] == id:
            p_quest = [q for q in participant['quests'] if q['quest']==quest ]
            if len(p_quest) == 0:
                p_quest = {'quest':quest, 'part1': -1, 'part2': -1, 'part3': -1}
                participant['quests'] += [p_quest]
            else:
                p_quest = p_quest[0]
            if part == 1:
                p_quest['part1'] = time
            elif part == 2:
                p_quest['part2'] = time
            else:
                p_quest['part3'] = time
# Now go quest by quest and add in the times
for q in quests:
    #current_quest = [x for x in participants if x['quests']['quest'] == q]
    quest_competitors = []
    for participant in participants:
        p_quest = [x for x in participant['quests'] if x['quest']==q]
        if len(p_quest) > 0:
            quest_competitors += [participant]
    
    for participant in quest_competitors:
        participant['total_time'] = -1
    for participant in quest_competitors:
        p_quest = [x for x in participant['quests'] if x['quest']==q][0]
        
        if p_quest['part1'] != -1:
            participant['total_time'] = p_quest['part1']
    quest_competitors = sorted(quest_competitors, key=lambda x: x['total_time'])
    # Start at 50 points
    step = 1
    points = 50
    for idx, competitor in enumerate(quest_competitors):
        if competitor['total_time'] == -1:
            continue
        
        if idx == 0:
            competitor['score'] += points
        else:
            # Look at the previous value, see if it's the same
            if competitor['total_time'] == quest_competitors[idx - 1]['total_time']:
                step += 1
                competitor['score'] += points
            else:
                if quest_competitors[idx - 1]['total_time'] != -1:
                    points -= step
                step = 1
                if points < 0:
                    points = 0
                competitor['score'] += points
    # Part 2
    for participant in quest_competitors:
            participant['total_time'] = -1
    for participant in quest_competitors:
        p_quest = [x for x in participant['quests'] if x['quest']==q][0]
        
        if p_quest['part2'] != -1:
            participant['total_time'] = p_quest['part1'] + p_quest['part2']

    quest_competitors = sorted(quest_competitors, key=lambda x: x['total_time'])
    step = 1
    points = 100
    for idx, competitor in enumerate(quest_competitors):
        if competitor['total_time'] == -1:
            continue
        
        if idx == 0:
            competitor['score'] += points
        else:
            # Look at the previous value, see if it's the same
            if competitor['total_time'] == quest_competitors[idx - 1]['total_time']:
                step += 1
                competitor['score'] += points
            else:
                if quest_competitors[idx - 1]['total_time'] != -1:
                    points -= step
                step = 1
                if points < 0:
                    points = 0
                competitor['score'] += points
    # Part 3
    for participant in quest_competitors:
            participant['total_time'] = -1
    for participant in quest_competitors:
        p_quest = [x for x in participant['quests'] if x['quest']==q][0]
        
        if p_quest['part3'] != -1:
            participant['total_time'] = p_quest['part1'] + p_quest['part2'] + p_quest['part3']

    quest_competitors = sorted(quest_competitors, key=lambda x: x['total_time'])
    step = 1
    points = 150
    for idx, competitor in enumerate(quest_competitors):

        if competitor['total_time'] == -1:
            continue
        
        if idx == 0:
            competitor['score'] += points
        else:
            # Look at the previous value, see if it's the same
            if competitor['total_time'] == quest_competitors[idx - 1]['total_time']:
                step += 1
                competitor['score'] += points
            else:
                if quest_competitors[idx - 1]['total_time'] != -1:
                    points -= step
                step = 1
                if points < 0:
                    points = 0
                competitor['score'] += points
    

# Sort the dictionary
participants = sorted(participants, key=lambda x: -x['score'])
# calculate checksum
checksum = 0
points = 1
step = 1
for idx, participant in enumerate(participants):
    # checksum += (x + 1)*participant['score']
    if idx == 0:
        checksum += participant['score']
        continue
    if participant['score'] == participants[idx - 1]['score']:
        step += 1
        checksum += participant['score'] * points
    else:
        points += step
        checksum += participant['score'] * points
        step = 1


print('Part 3: checksum = ' + str(checksum))
