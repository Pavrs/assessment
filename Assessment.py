#outside makes this global data
print('Binary search starts after this line: ')       #seperates the results for the binary search and the linear search
arr = [1,2,3,4,5,6,7,8,9,10]        
print(arr)          #prints a displayed list
target= int(input('Please input any number you want to find in the list above: '))       #requires user input to find required number in the list

def binary(arr, target): #local data for binary search
    left, right = 0, len(arr)-1 #sets up first number and last index number in the list 
    while left<=right:
        mid = (left+right)//2   #finds the middle between last number and first number
        if arr[mid]==target:    #finds the target 
            return mid
        elif arr[mid]<target:   #eliminates left hand side of data if target above the middle
            left= mid+1
        else:                   #eliminates right hand side of data if target bellow the middle
            right= mid-1
    return -1

result= binary(arr, target)     #finds the index the target is found on

if result != -1:        #proves if target is in the list and outputs the results
    print(f' The target {target} is found at the index {result}')
else:
    print(f' {target} was not found in the list')


#local data for linear search
def linear():

    for index in range(len(arr)):       #searches for the target in the required number of operations to find the target
        result = index      # sets the result as the index
        if arr[index] == target:        # outputs the target and the index when the target is found
            print(f' The target {target} is found at the index {result}')
            break
        else:               #outputs the results if the target is not found at that current index or in the entire list
            print(f' {target} was not found in the list')

print('Linear search starts after this line: ')       #seperates the results for the binary search and the linear search
linear()
