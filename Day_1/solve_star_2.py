with open("input.txt", "r") as file:
    # Initialize two empty lists to store the values from each column
    ascendList = []
    descendList = []

    # Read each line in the file
    for line in file:
        # Split each line into separate values
        values = line.split()
        # Append the first value to list1 and the second value to list2
        ascendList.append(int(values[0]))
        descendList.append(int(values[1]))

######################### Beginning of code ############################

numbOfOccur = 0

concatList = ascendList + descendList

concatList.sort()

concatSet = set(ascendList)

for numb in concatSet:
    
    occrFirstList = ascendList.count(numb)
    occrSecondList = descendList.count(numb)

    numbOfOccur += numb * occrFirstList *  occrSecondList

print(f"total numbers: {numbOfOccur}")
    

