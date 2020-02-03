import sys
import random


n = int(sys.argv[1])

with open('input.in', 'w') as f_out:
    generated = []
    for i in range(n):
        x = random.randint(0, n-1)
        while x in generated:
            x = random.randint(0, n-1)
        generated.append(x)
        f_out.write(f'{x}\n')
        
    for i in range(n):
        x = random.randint(0, n-1)
        f_out.write(f'{x}\n')