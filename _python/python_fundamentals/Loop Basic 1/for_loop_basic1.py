# Python Stack Assignments
# Loop Basics
# Anas Zughayyar

# 1. Basic 
print("# 1. Basic ")

for i in range(0,151,1):
    print(i)

# 2. Multiples of Five
print("# 2. Multiples of Five")

for i in range(5,1001,5):
    print(i)

# 3. Counting, the Dojo Way
print("# 3. Counting, the Dojo Way")

for i in range(1,101,1):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# 4. Whoa. That Sucker's huge
print("# 4. Whoa. That Sucker's huge")

sum = 0
for k in range(0,500001,1):
    if k % 2 != 0:
        sum = sum + k
print("Final sum = ", sum)

# 5. Countdown by Fours
print("# 5. Countdown by Fours")

for i in range(2018,0,-4):
    print(i)

# 6. Flexiblge Counter
print("# 6. Flexiblge Counter")

lowNum = 2
highNum = 9
mult = 3
for n in range(lowNum,highNum+1,1):
    if n % mult == 0:
        print(n)