f = open('a.txt', 'r')
line = "  "
xPos, yPos = 0 , 0
while (line != ''):
    line = f.readline().strip()
    if(line.startswith("f")):
        xPos += int(line[-1])
    elif(line.startswith("u")):
        yPos -= int(line[-1])
    elif(line.startswith("d")):
        yPos += int(line[-1])
print(xPos*yPos)
f.close()


