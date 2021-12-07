try : 
    file = open('day1.txt')
except :
    print('yo its not loading the stupid input file joey')
    exit()

lineValue = 999999999
nIncreases = 0 

for line in file:
    line = int(line)
    if line > lineValue :
        nIncreases = nIncreases + 1
    lineValue = line

print("Total increases:")
print(nIncreases)