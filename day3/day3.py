
##===============getting puzzle input===============##
import puzzle as pz
lines = pz.get() #list of string lines
linesClone = pz.get()
linesClone2 = pz.get()
##===================variables======================##
gamma, epsilon = '', '' #strings
o2Rate, co2Rate = '', ''
lengthOfLines = len(lines[0])
#?==================functions=======================##
def toDecimal(*args):#multiple argument
    return [int(arg, base=2) for arg in args]# for every argument convert decimal integer and put them in to a list
#!======================Part1=============================##

for i in range(lengthOfLines):#for every index of numb
    digit = [line[i] for line in lines]
    #print(digit, digit.count('0'))
    if digit.count('0') > len(lines)/2:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

gamma, epsilon = toDecimal(gamma, epsilon)# returned list [1300, 2795]
part1 = gamma * epsilon
print(part1)
#!========================Part2============================#

for j in range(lengthOfLines):
    digit = [line[j] for line in linesClone]
    mostCommonBit = '1' if digit.count('1') >= len(linesClone)/2 else '0'
    linesClone = [line for line in linesClone if line[j] == mostCommonBit]
    if len(linesClone) == 1:
        o2Rate = linesClone[0]
        break

for j in range(lengthOfLines):
    digit = [line[j] for line in linesClone2] 
    leastCommonBit = '0' if digit.count('1') >= len(linesClone2)/2  else '1'
    linesClone2 = [line for line in linesClone2 if line[j] == leastCommonBit]
    if len(linesClone2) == 1:
        co2Rate = linesClone2[0]
        break

o2Rate, co2Rate = toDecimal(o2Rate, co2Rate)
part2 = o2Rate * co2Rate
print(part2)
