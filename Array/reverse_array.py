Array1 = ["MCA","BCA","12th","10th"]
tempReverseArray = []
for i in range(len(Array1)-1,-1,-1):
    tempReverseArray.append(Array1[i])
print("Print Array Using For loop Reverse Array",tempReverseArray)    
Array1.reverse() # return True or false
print("Print Array Using Reverse Method ",Array1)
