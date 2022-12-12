ar = []
gamma = []
epsilon = []
#This is for reading file and put it into an array
with open('c.txt') as f:
    for line in f.readlines():
        ar.append(line.strip())
#This is for calculating gamma number
for x in range(len(line)-1):
    total = 0
    for y in range(len(ar)):
        total += int(ar[y][x])
        if (total>(len(ar)/2)):
            gamma.append("1")
            break
    if (total < (len(ar)/ 2)):
        gamma.append("0")
#This is for converting (array or list)gamma to a string
gamma = ''.join(gamma)
for i in range(len(line)-1):
    if (gamma[i] == '1'):
        epsilon.append("0")
    else:
        epsilon.append("1")
gamma = int(gamma, base=2)
epsilon = ''.join(epsilon)
epsilon = int(epsilon, base=2)
print("Power consumption of the submarine is",epsilon*gamma)
