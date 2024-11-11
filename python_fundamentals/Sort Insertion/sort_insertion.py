########################
#### Anas Zughayyar ####
########################
#### Selection Sort ####
########################

x = [6,5,3,1,8,7,2,4]
list_1 = [8,5,2,6,9,3,1,4,0,7]

def sort_insertion(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while key < arr[j] and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(sort_insertion(x))
print(sort_insertion(list_1))
