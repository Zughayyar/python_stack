############################
#####  Anas Zughayyar  #####
############################
### Assignment: MathDojo ###
############################
### file name: MathDojo ####
############################

class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        add_nums = 0
        for i in nums:
            add_nums += i
        self.result = self.result + num + add_nums
        return self
    def subtract(self, num, *nums):
        sub_nums = 0
        for i in nums:
            sub_nums += i
        self.result = self.result - num - sub_nums
        return self

if __name__ == "__main__":

    # test add function (result = 100):
    md_add = MathDojo()
    test_add = md_add.add(10,10,10).add(5,5,5,5).add(50).result
    print(test_add)

    # test subtract function (result = -100):
    md_sub= MathDojo()
    test_sub = md_sub.subtract(10,10,10).subtract(5,5,5,5).subtract(50).result
    print(test_sub)

    # create an instance:
    md = MathDojo()
    x = md.add(2).add(2,5,1).subtract(3,2).result
    print(x)
