ArrayData = [10,40,20,60,20,40,30,12,100,110,200,34,30,6]
MinNumber = ArrayData[0]
MaxNumber = ArrayData[1]
i = len(ArrayData) - 1
while i >= 0:
    if(MinNumber >= ArrayData[i]):
        MinNumber = ArrayData[i]
    if(MaxNumber <= ArrayData[i]):
        MaxNumber = ArrayData[i]
    i -= 1
print("Using While loop For Find Min ",MinNumber)
print("Using While loop For Find Max ",MaxNumber)