myArray = [10, 20, 3, 4, 1, 100, 0]
n = len(myArray)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if myArray[j] > myArray[j+1]:
            myArray[j], myArray[j+1] = myArray[j+1], myArray[j]
            swapped = True
    if not swapped:
        break
print(myArray)