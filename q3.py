def calc_number(standard, vote):
    current_number = 0
    for x in range(len(vote)):
        current_digit = int(vote[x]) * int(standard[x % len(standard)]) ** x
        current_number += current_digit
    return current_number


f = open ('q3p1.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
total_score = 0


for item in raw_input:
    [standard, vote] = item.split(' ')
    standard = standard.split('-')[1][::-1]
    vote = vote[::-1]
    total_score += calc_number(standard, vote)
print('Part 1: total score is ' + str(total_score))

f = open ('q3p2.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
total_score = 0

for item in raw_input:
    [standard, vote] = item.split(' ')
    standard = standard.split('-')[1][::-1]
    vote = vote[::-1]
    
    total_score += calc_number(standard, vote)
print('Part 2: total score is ' + str(total_score))

f = open ('q3p3.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
total_score = 0



for item in raw_input:
    [standard, vote] = item.split(' ')
    standard = standard.split('-')[1][::-1]
    vote = vote[::-1]
    original_number = calc_number(standard, vote)
    # Determine if valid
    lower_bound = int(str(original_number))
    upper_bound = int(vote[::-1])
    valid = True
    for x in range(lower_bound, upper_bound):
        new_number = calc_number(standard, str(x)[::-1])
        if new_number == original_number:
            valid = False
            break
    if valid == True:
        total_score += original_number

    
print('Part 3: total score is ' + str(total_score))