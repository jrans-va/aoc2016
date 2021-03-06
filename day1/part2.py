input = "R4, R5, L5, L5, L3, R2, R1, R1, L5, R5, R2, L1, L3, L4, R3, L1, L1, R2, R3, R3, R1, L3, L5, R3, R1, L1, R1, R2, L1, L4, L5, R4, R2, L192, R5, L2, R53, R1, L5, R73, R5, L5, R186, L3, L2, R1, R3, L3, L3, R1, L4, L2, R3, L5, R4, R3, R1, L1, R5, R2, R1, R1, R1, R3, R2, L1, R5, R1, L5, R2, L2, L4, R3, L1, R4, L5, R4, R3, L5, L3, R4, R2, L5, L5, R2, R3, R5, R4, R2, R1, L1, L5, L2, L3, L4, L5, L4, L5, L1, R3, R4, R5, R3, L5, L4, L3, L1, L4, R2, R5, R5, R4, L2, L4, R3, R1, L2, R5, L5, R1, R1, L1, L5, L5, L2, L1, R5, R2, L4, L1, R4, R3, L3, R1, R5, L1, L4, R2, L3, R5, R3, R1, L3"
directions = [i.strip() for i in input.split(",")]

location = [0, 0]
direction = 'N'

turns = {
    'N': {
        'R': 'E',
        'L': 'W',
        'x': 0,
        'y': 1
    },
    'E': {
        'R': 'S',
        'L': 'N',
        'x': 1,
        'y': 0
    },
    'S': {
        'R': 'W',
        'L': 'E',
        'x': 0,
        'y': -1
    },
    'W': {
        'R': 'N',
        'L': 'S',
        'x': -1,
        'y': 0
    }
}

prev_locations = []

for d in directions:
    direction = turns[direction][d[0]]
    if direction in ['N', 'S']:
        for _ in xrange(int(d[1:])):
            location[1] += turns[direction]['y']
            if tuple(location) in prev_locations:
                print location
                exit()
            prev_locations.append((location[0], location[1]))
    else:
        for _ in xrange(int(d[1:])):
            location[0] += turns[direction]['x']
            if tuple(location) in prev_locations:
                print location
                exit()
            prev_locations.append((location[0], location[1]))


