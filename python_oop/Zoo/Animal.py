##################################
######### Anas Zughayyar #########
##################################
#### Python Stack Assignments ####
##################################
##########     Zoo     ###########
##################################

## Class Animal

class Animal:
    def __init__(self, name, age, health_level, happiness_level):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level
    
    def display_info(self):
        print("Animal family:", self.family)
        print("Animal name:", self.name)
        print("Animal health:", self.health_level)
        print("Animal hapiness level:", self.happiness_level)