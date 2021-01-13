# Python program to Move All -ve Element At End 
# Without changing order Of Array Element 

# Moves all -ve element to end of array in 
# same order. 
def segregateElements(arr, n): 
	# Create an empty array to store result 
	temp = [0 for k in range(n)] 

	# Traversal array and store +ve element in 
	# temp array 
	j = 0 # index of temp 
	for i in range(n): 
		if (arr[i] >= 0 ): 
			temp[j] = arr[i] 
			j +=1

	# If array contains all positive or all negative. 
	if (j == n or j == 0): 
		return

	# Store -ve element in temp array 
	for i in range(n): 
		if (arr[i] < 0): 
			temp[j] = arr[i] 
			j +=1

	# Copy contents of temp[] to arr[] 
	for k in range(n): 
		arr[k] = temp[k] 

# Driver program 
arr = [1 ,-1 ,-3 , -2, 7, 5, 11, 6 ] 
n = len(arr) 

segregateElements(arr, n); 

for i in range(n): 
	print(arr[i]) 

# Contributed by Afzal aka Saan 
