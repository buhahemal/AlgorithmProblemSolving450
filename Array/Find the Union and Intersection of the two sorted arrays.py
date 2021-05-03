def getDistinctArr(arr):
    return (list(set(arr)))
def uniontwoArray(arr1,arr2):
    print(len(getDistinctArr(arr1 + arr2)))
def intersectiontwoArray(arr1,arr2):
    n = len(arr1)
    m = len(arr2)
    result = []
    for i in range(0,n):
        for j in range(0,m):
            if(arr1[i] == arr2[j]):
                result.append(arr1[i])
                break
    print(result)
arra = [85,25,25,1,32,54,6]
arrb = [85,2,1]
uniontwoArray(arra,arrb)
intersectiontwoArray(arra,arrb)