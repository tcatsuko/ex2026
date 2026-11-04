f = open ('q2p1.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
groups = []
checksum = 0
for note_line in raw_input:
    notes = note_line.split(' ')
    # First get the digits in there
    digits = set()
    for note in notes:
        left = int(note[0])
        right = int(note[2])
        comparison = note[1]
        digits.add(left)
        digits.add(right)
    digits = list(digits)
    # Now, start to do the sort
    changes_made = True
    while changes_made == True:
        changes_made = False
        for note in notes:
                left = int(note[0])
                right = int(note[2])
                comparison = note[1]
                left_index = digits.index(left)
                right_index = digits.index(right)
                if comparison == '>':
                    if left_index < right_index:
                         changes_made = True
                         digits.pop(left_index)
                         digits.insert(right_index, left)
                elif comparison == '<':
                    if left_index > right_index:
                         changes_made = True
                         digits.pop(left_index)
                         digits.insert(right_index, left)
    digits = digits[::-1]
    # Combine into a number
    digits = int(''.join([str(x) for x in digits]))
    checksum += digits
print('Part 1: checksum is ' + str(checksum))
                      
f = open ('q2p2.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
groups = []
checksum = 0
for note_line in raw_input:
    notes = note_line.split(' ')
    # First get the digits in there
    digits = set()
    for note in notes:
        left = int(note[0])
        right = int(note[2])
        comparison = note[1]
        digits.add(left)
        digits.add(right)
    digits = list(digits)
    # Now, start to do the sort
    changes_made = True
    while changes_made == True:
        changes_made = False
        for note in notes:
                left = int(note[0])
                right = int(note[2])
                comparison = note[1]
                left_index = digits.index(left)
                right_index = digits.index(right)
                if comparison == '>':
                    if left_index < right_index:
                         changes_made = True
                         digits.pop(left_index)
                         digits.insert(right_index, left)
                elif comparison == '<':
                    if left_index > right_index:
                         changes_made = True
                         digits.pop(left_index)
                         digits.insert(right_index, left)
    digits = digits[::-1]
    # Combine into a number
    digits = int(''.join([str(x) for x in digits]))
    checksum += digits
print('Part 2: checksum is ' + str(checksum))
                      
f = open ('q2p3.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
groups = []
checksum = 0
for note_line in raw_input:
    notes = note_line.split(' ')
    # First get the digits in there
    digits = set()
    for note in notes:
        left = int(note[0])
        right = int(note[2])
        comparison = note[1]
        digits.add(left)
        digits.add(right)
    digits = list(digits)
    # Now, start to do the sort
    changes_made = True
    while changes_made == True:
        changes_made = False
        for note in notes:
                left = int(note[0])
                right = int(note[2])
                comparison = note[1]
                left_index = digits.index(left)
                right_index = digits.index(right)
                if comparison == '>':
                    if left_index < right_index:
                         changes_made = True
                         digits.pop(right_index)
                         digits.insert(left_index, right)
                         
                elif comparison == '<':
                    if left_index > right_index:
                         changes_made = True
                         digits.pop(left_index)
                         digits.insert(right_index, left)
               
                          

    digits = digits[::-1]
    # Combine into a number
    digits = int(''.join([str(x) for x in digits]))
    checksum += digits
print('Part 3: checksum is ' + str(checksum)) 