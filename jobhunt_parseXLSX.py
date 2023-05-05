# Job Hunt Contacts from XLS File Formats

import pandas as pd

# Pandas to parse file
file = 'SK5000-max-empl.xlsx'       #Replace with desired xlsx file
excel_file = pd.read_excel(file)

def write_text_file(string):
    for index, row in excel_file.iterrows():
        row = [str(element) for element in row]
        if any(string in box for box in row):
            write_to_file = str(index) + '\n \n' + str(row) + '\n \n'
            with open ('List_BigEmployeeNums.txt','a') as file:        #Replace with desired output file
                file.write(write_to_file)

#Run functions + replace strings with desired search parameters
write_text_file('Technology')
write_text_file('Software')
write_text_file('Computer')
write_text_file('Security')
write_text_file('IT')
write_text_file('Cyber')
write_text_file('CISO')
write_text_file('Engineer')
write_text_file('Engineering')


### Making files more readable // Searching different parameters
remove1 = "'nan'"

with open('List_Execs.txt','r') as file:
    for line in file:
        if remove1 in line:
            line.replace(remove1,"")
            print(line)

with open('List3.txt','r') as file:
    for line in file:
        if 'Hiring' in line or 'Recruiter' in line:
            print(line)
