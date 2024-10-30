##################################
######### Anas Zughayyar #########
##################################
#### Python Stack Assignments ####
##################################
##########     Zoo     ###########
##################################

## import the Animal Class:
from Animal import Animal

# Class Tiger
class Tiger(Animal):
    def __init__(self, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)
        self.family = "Tigers"

    def feed(self):
        self.happiness_level += 10
        self.health_level += 10