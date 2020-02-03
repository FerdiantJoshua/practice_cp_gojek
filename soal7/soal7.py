output_filename = 'output.txt'
f_out = open('output.txt', 'w')

def permutations():
    global running
    global characters
    global bitmask
    global f_out
    if len(running) == len(characters):
        print(''.join(running), file=f_out)
    else:
        for i in range(len(characters)):
            if ((bitmask>>i)&1) == 0:
                bitmask |= 1<<i
                running.append(characters[i])
                permutations()
                bitmask ^= 1<<i
                running.pop()

raw = input()
characters = list(raw)
running = []
bitmask = 0
permutations()
f_out.close()