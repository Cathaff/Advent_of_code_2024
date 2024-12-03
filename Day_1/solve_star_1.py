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

######################### Beginning the code ############################

left = 0
distance = 0

ascendList.sort()

descendList.sort(reverse=True)

concatList = ascendList + descendList

right = len(concatList)  - 1

while left <  right :
    distance += abs(concatList[left] - concatList[right])
    left += 1
    right -= 1

print(f"total: {distance}")

