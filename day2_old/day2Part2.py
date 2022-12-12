f = open('day2Part2.txt', 'r')
line = "  "
xPos, yPos, aim = [0] * 3
while (line != ''):
    line = f.readline().strip()
    if(line.startswith("f")):
        xPos += int(line[-1])
        yPos += aim * int(line[-1])
    elif(line.startswith("u")):
        aim -= int(line[-1])
    elif(line.startswith("d")):
        aim += int(line[-1])
print(xPos*yPos)
f.close()
