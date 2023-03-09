'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
'''
usernum = int(input("Choose a number: "))
allnum = range(1, usernum)
divisors = []

for x in allnum:
    if usernum % x == 0:
        divisors.append(x)

print(divisors)
