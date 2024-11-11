###Python Stack###
###Assignment###
###Functions Basic 2###
###Anas Zughayyar###


# 1. Countdown
print("### 1. Countdown")

def count_down(num):
    new_list = []
    for i in range(num,-1,-1):
        new_list.append(i)
    return new_list
print(count_down(5))


# 2. Print and Return
print("### 2. Print and Return")

def print_and_return(list1):
    print([list1[0]])
    return list1[1]
new_print = print_and_return([1,2])
print(new_print)


# 3. First Plus Length
print("### 3. First Plus Length")

def first_plus_length(list2):
    return list2[0] + len(list2)
print(first_plus_length([1,2,3,4,5]))


# 4. Values Greater than Second
print("### 4. Values Greater than Second")

def vlaues_greater_than_second(list3):
    new_list3 = []
    if len(list3) < 2:
        return False
    else:
        for i in range(0,len(list3),1):
            if list3[i] > list3[1]:
                new_list3.append(list3[i])
        return new_list3
print(vlaues_greater_than_second([5,2,3,2,1,4]))
print(vlaues_greater_than_second([3]))

# 5. This Length, That Value
print("### 5. This Length, That Value")

def length_and_value(size,value):
    new_list = []
    for i in range(0,size,1):
        new_list.append(value)
    return new_list
print(length_and_value(4,7))
print(length_and_value(6,2))