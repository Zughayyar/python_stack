########################
#### Anas Zughayyar ####
########################
#### Insertion Sort ####
########################

def sort_selection(some_list):
    for i in range(len(some_list)):
        for j in range(i,len(some_list)):
            if some_list[i] > some_list[j]:
                some_list[i] , some_list[j] = some_list[j] , some_list[i]
    return some_list

list_1 = [8,5,2,6,9,3,1,4,0,7]
list_2 = [81,53,12,-6,53,3,1,4,-2,7]
