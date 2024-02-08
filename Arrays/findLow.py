myArray = [100, 4, 2, 8, 10, 1, 9]
minVal = myArray[0]
for i in myArray:
    if i < minVal:
        minVal = i
print("Lowest Value: ", minVal)