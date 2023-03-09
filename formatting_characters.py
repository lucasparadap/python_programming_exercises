'''
https://docs.python.org/3/tutorial/inputoutput.html
:<  |  Left Aligned
:>  |  Right Aligned
:^  |  Center Aligned
:f  |  Fix Point (decimal)(float)
:x  |  Hex Format (lower case)
:X  |  Hex Format (upper case)
:#d |  Num of Digits formatted Right
'''


mydict = {'Crypto':3,'Systems':5,'Networking':5, \
'Gov-Risk-Comp':2,'Threat Intel':2,'Python':2, \
'Logs':3,'AppSec':2,'Capstone':1}

print("{:^15}\t{:^7}".format("Course","Modules"))     #Title Bar
print("{:^15}\t{:^7}".format("-"*15,"-"*7))           #Spacing format of elements

for course in mydict.keys():                                #Loop to return elements
    print("{:^15}\t{:^7}".format(course,mydict[course]))
#----------------------------------------------------------------------------------------------------------------
print(f'{"-"*25:<}\n')                                    #example of f string formatting - BELOW IS F STRING REWRITE

print(f'{"Course":^20}\t{"Modules":^10}')
print(f'{"-"*20:^20}\t{"-"*10:^10}')                    #This is the exact same thing but with F-String

for course in mydict.keys():
    print(f'{course:^20}\t{mydict[course]:^10}')
