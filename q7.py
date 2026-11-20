import math
import copy

def run_stage(clouds, impulses, explosion = math.inf):
    # impulses[]
    ## Inside each item:
    ## {strength: int, recipients:[{id, num_impulses}]}
    new_impulses = []
    for impulse in impulses:
        strength = impulse['strength']
        recipients = impulse['recipients']
        for recipient in recipients:
            id = recipient['id']
            
            num_impulses = recipient['num_impulses']
            # Now, add the energy 
            if id in clouds.keys():
                cloud = clouds[id]
            else:
                continue
            cloud['energy'] += (strength * num_impulses)
            if strength > 1:
                # Need to start sending these out
                next_strength = strength - 1
                # Check to see if this impulse is already in next_impulses
                if len([x for x in new_impulses if x['strength'] == next_strength]) == 0:
                    new_impulses += [{'strength': next_strength, 'recipients':[]}]
                new_impulse = [x for x in new_impulses if x['strength'] == next_strength][0]
                new_impulse_recipients = new_impulse['recipients']
                for downstream in clouds[id]['connections']:
                    if len([x for x in new_impulse_recipients if x['id'] == downstream]) == 0:
                        new_impulse_recipients += [{'id':downstream, 'num_impulses': 0}]
                    set_impulse = [x for x in new_impulse_recipients if x['id'] == downstream][0]
                    set_impulse['num_impulses'] += num_impulses
    # Once all of this is done need to set up explosions
    exploded_clouds = []
    for key, cloud in clouds.items():
        if cloud['energy'] >= explosion:
            exploded_clouds += [key]
            if len([x for x in new_impulses if x['strength'] == 10]) == 0:
                new_impulses += [{'strength': 10, 'recipients': []}]
            new_impulse = [x for x in new_impulses if x['strength'] == 10][0]
            new_impulse_recipients = new_impulse['recipients']
            for downstream in cloud['connections']:
                if len([x for x in new_impulse_recipients if x['id'] == downstream]) == 0:
                    new_impulse_recipients += [{'id':downstream, 'num_impulses': 0}]
                set_impulse = [x for x in new_impulse_recipients if x['id'] == downstream][0]
                set_impulse['num_impulses'] += 1
    for item in exploded_clouds:
        # remove these from the clouds list
        clouds.pop(item)
    return new_impulses


f = open('q7p1.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
clouds = {}
for line in raw_input:
    cloud_data = line.split(', ')
    id = cloud_data[0].split('=')[1]
    energy = int(cloud_data[1].split('=')[1])
    connections = cloud_data[2].split('=')[1].split(',')
    cloud = {}
    cloud['energy'] = energy
    cloud['connections'] = connections
    clouds[id] = cloud
# Find the cloud with the most connections
max_conn = 0
for key, value in clouds.items():
    if len(value['connections']) > max_conn:
        top_cloud = key


# Test case
for key, value in clouds.items():
    if len(value['connections']) > max_conn:
        top_cloud = key
        max_conn = len(value['connections'])

impulses = [{'strength':5, 'recipients': [{'id': top_cloud, 'num_impulses': 1}]}]
while len(impulses) > 0:
    new_impulses = run_stage(clouds, impulses)
    impulses = new_impulses
total_energy = 0
for key, value in clouds.items():
    total_energy += value['energy']
print('Part 1: the total energy of all the clouds is ' + str(total_energy))

f = open('q7p2.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
clouds = {}
for line in raw_input:
    cloud_data = line.split(', ')
    id = cloud_data[0].split('=')[1]
    energy = int(cloud_data[1].split('=')[1])
    connections = cloud_data[2].split('=')[1].split(',')
    cloud = {}
    cloud['energy'] = energy
    cloud['connections'] = connections
    clouds[id] = cloud
# Find the cloud with the most connections
max_conn = 0
for key, value in clouds.items():
    if len(value['connections']) > max_conn:
        top_cloud = key


# Test case
for key, value in clouds.items():
    if len(value['connections']) > max_conn:
        top_cloud = key
        max_conn = len(value['connections'])

impulses = [{'strength':10, 'recipients': [{'id': top_cloud, 'num_impulses': 1}]}]
while len(impulses) > 0:
    new_impulses = run_stage(clouds, impulses)
    impulses = new_impulses
total_energy = 0
for key, value in clouds.items():
    total_energy += value['energy']
print('Part 2: the total energy of all the clouds is ' + str(total_energy))

f = open('q7p3.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
clouds = {}
for line in raw_input:
    cloud_data = line.split(', ')
    id = cloud_data[0].split('=')[1]
    energy = int(cloud_data[1].split('=')[1])
    connections = cloud_data[2].split('=')[1].split(',')
    cloud = {}
    cloud['energy'] = energy
    cloud['connections'] = connections
    clouds[id] = cloud
# Find the cloud with the most connections

max_energy = 0
# Start at each cloud, find out which is the least-worst to start with
for cloud_id in clouds.keys():
    clouds_copy = copy.deepcopy(clouds)
    impulses = [{'strength':10, 'recipients': [{'id': cloud_id, 'num_impulses': 1}]}]
    while len(impulses) > 0:
        new_impulses = run_stage(clouds_copy, impulses, 1000000)
        impulses = new_impulses
    total_energy = 0
    for key, value in clouds_copy.items():
        total_energy += value['energy']
    if total_energy > max_energy:
        max_energy = total_energy
print('Part 3: max energy is ' + str(max_energy))