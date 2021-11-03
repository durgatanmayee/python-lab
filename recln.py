def recurlinear(arr,x):
    for i in range (len(arr)):
        if arr[i] == x:
            return i
        else:
            return recurlinear(arr[i+1: ],x)
    return -1
print(recurlinear([56,45,62,23,14],62))
