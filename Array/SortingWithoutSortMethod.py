#Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
#SortArray = [30,10,20]
def SortArray(arr): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1):
          if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
SortArrayData = [30,10,20]
SortArray(SortArrayData)
print(SortArrayData)