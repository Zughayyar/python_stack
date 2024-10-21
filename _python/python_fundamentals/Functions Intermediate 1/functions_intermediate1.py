### Python Stack    ###
### Assignment      ###
### Functions Intermediate 1    ###
### Anas Zughayyar  ###

import random
def randInt(min = None, max= None):
    num = random.random()
    if (min == None) and (max == None):
        return round(num * 100)
    elif (min == None) and (max != None):
        if max < 0:
            return 'Max is less than Zero !!'
        else:
            return round(num * max)
    elif (min != None) and (max == None):
        return round((num * (100-min)) + min)
    else:
        if min > max:
            return 'min value is bigger than max !!'
        else:
            return round((num * (max - min)) + min)

print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50,max=500))
print(randInt(min=5000,max=500))
print(randInt(max=-25))
print(randInt(min=-50,max=500))
