lines = [l.strip() for l in open('input.txt').readlines()]
pword = "abcdefgh"

def swap_pos(s, x, y):
    at_x = s[x]
    at_y = s[y]
    result = s[:x] + at_y + s[x+1:]
    result = result[:y] + at_x + result[y+1:]
    return result

def swap_letter(s, x, y):
    x_index = s.find(x)
    y_index = s.find(y)
    return swap_pos(s, x_index, y_index)

def rotate_left(s, steps):
    return s[steps:] + s[:steps]

def rotate_right(s, steps):
    return s[len(s)-steps:] + s[:len(s)-steps]

def rotate_pos(s, x):
    pos = s.find(x)
    if pos >= 4:
        pos += 1
    return rotate_right(s, pos+1)

def reverse(s, x, y):
    return s[:x] + s[x:y+1][::-1] + s[y+1:]

def move(s, x, y):
    char = s[x]
    result = s[:x] + s[x+1:]
    return result[:y] + char + result[y:]


for line in lines:
    parts = line.split()
    if parts[0] == 'swap':
        if parts[1] == 'position':
            pword = swap_pos(pword, int(parts[2]), int(parts[5]))
        else:
            pword = swap_letter(pword, parts[2], parts[5])
    elif parts[0] == 'rotate':
        if parts[1] == 'left':
            pword = rotate_left(pword, int(parts[2]))
        elif parts[1] == 'right':
            pword = rotate_right(pword, int(parts[2]))
        else:
            pword = rotate_pos(pword, parts[-1])
    elif parts[0] == 'reverse':
        pword = reverse(pword, int(parts[2]), int(parts[4]))
    elif parts[0] == 'move':
        pword = move(pword, int(parts[2]), int(parts[5]))


print pword

