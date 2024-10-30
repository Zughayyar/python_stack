##################################
######### Anas Zughayyar #########
##################################
#### Python Stack Assignments ####
##################################
##########     Zoo     ###########
##################################

## import the Animal Class:
from Animal import Animal


## Class Lion
class Lion(Animal):
    def __init__(self, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)
        self.family = "Lions"

    def feed(self):
        self.happiness_level += 20
        self.health_level += 20

