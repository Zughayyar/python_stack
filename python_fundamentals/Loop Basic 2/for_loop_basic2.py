### Python Stack    ###
### Assignment      ###
### Loop Basic 2    ###
### Anas Zughayyar  ###

# 1. Boggie Size:
print("##### 1. Boggie Size:")
def biggie_size(list1):
    for i in range(0,len(list1),1):
        if list1[i] > 0 :
            list1[i] = "big"
    return list1
print(biggie_size([-1,3,4,-5]))


# 2. Count Positives:
print("##### 2. Count Positives")
def count_positives(list2):
    count = 0
    for i in range(0,len(list2),1):
        if list2[i] > 0:
            count += 1
    list2[len(list2) - 1] = count
    return list2
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))


# 3. Sum Total:
print("##### 3. Sum Total:")
def sum_total(list1):
    sum = 0
    for i in range(0,len(list1),1):
        sum += list1[i]
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))


# 4. Average 
print("##### 4. Average")
def average(list1):
    sum = 0
    for i in range(0,len(list1),1):
        sum += list1[i]
    return sum / len(list1)
print(average([1,2,3,4]))


# 5. Length:
print("##### 5. Length:")
def length(list1):
    count = 0
    for i in list1:
        count += 1
    return count
print(length([37,2,1,-9]))
print(length([]))


# 6. Minimum
print("##### 6. Minimum")
def minimum(list1):
    if len(list1) == 0:
        return False
    else:
        min_num = list1[0]
        for i in list1:
            if min_num > i:
                min_num = i
    return min_num
print(minimum([37,2,1,-9]))
print(minimum([]))


# 7. Maximum
print("##### 7. Maximum")
def maximum(list1):
    if len(list1) == 0:
        return False
    else:
        max_num = list1[0]
        for i in list1:
            if max_num < i:
                max_num = i
    return max_num
print(maximum([37,2,1,-9]))
print(maximum([]))


# 8. Ultimate Analysis
print("##### 8. Ultimate Analysis")
def ultimate_analysis(list1):
    sum = 0
    min_num = list1[0]
    max_num = list1[0]
    for i in list1:
        sum += i
        if min_num > i:
            min_num = i
        if max_num < i:
            max_num = i
    return {
        'sumTotal': sum,
        'average': sum/len(list1),
        'minimum': min_num,
        'maximum': max_num
        }
print(ultimate_analysis([37,2,1,-9]))
        

# 9. Reverse List
print("##### 9. Reverse List")
def reverse_list(list1):
    left = 0
    right = len(list1) - 1
    while left < right:
        temp = list1[left]
        list1[left] = list1[right]
        list1[right] = temp
        left += 1
        right -= 1
    return list1
print(reverse_list([37,2,1,-9]))