##########################
##### Anas Zughayyar #####
##########################
###### Python Stack ######
##########################

### Assignment : Functions Intermediate 2 

x = [ [5,2,3] , [10,8,9] ]
students = [
    {'first_name': 'Michael' , 'last_name': 'Jordan'} ,
    {'first_name': 'John' , 'last_name': 'Rosales'} ,
    {'first_name': 'Mark' , 'last_name': 'Guillen'} ,
    {'first_name': 'KB' , 'last_name': 'Tonel'}
]
sports_directory = {
    'basketball' : ['Kobe' , 'Jordan' , 'James' , 'Curry'] ,
    'soccer' : ['Messi' , 'Ronaldo' , 'Rooney']
}
z = [ {'x': 10 , 'y': 20} ]

###################################################
##### Update Values in Dictionaries and Lists #####
###################################################
# 1. Change value 10 in x to 15
x[1][0] = 15
#print("x =" , x)

# 2. 
students[0]['last_name'] = 'Bryant'
#print(students)

# 3.
sports_directory['soccer'][0] = 'Andres'
#rint(sports_directory)

# 4.
z[0]['y'] = 30
#print(z)

##################################################
##### Iterate Through a List of Dictionaries #####
##################################################
def iterateDictionary(some_list):
    for i in some_list:
        print('first_name -', i['first_name'] + ', ' + 'last_name -' , i['last_name'])

iterateDictionary(students)

##################################################
##### Get Values From A List of Dictionaries #####
##################################################

def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#########################################################
##### Iterate Through a Dictionary with List Values #####
#########################################################

dojo = {
    'locations': ['San Jose', 
                  'Seattle', 
                  'Dallas', 
                  'Chicago', 
                  'Tulsa', 
                  'DC', 
                  'Burbank'
                  ],
    'instructors': ['Michael', 
                    'Amy', 
                    'Eduardo', 
                    'Josh', 
                    'Graham', 
                    'Patrick',
                    'Ming',
                    'Devon'
                    ]
}

def printInfo(some_dict):
    for i in some_dict:
        print(len(some_dict[i]), i.upper())
        for j in some_dict[i]:
            print(j)
    
printInfo(dojo)