'''
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.
'''

userinput = input("Write down any sentence: ")
if userinput.endswith("."):
    userinput = userinput.rstrip(".")
    punct = "."
elif userinput.endswith("?"):
    userinput = userinput.rstrip("?")
    punct = "?"
elif userinput.endswith("!"):
    userinput = userinput.rstrip("!")
    punct = "!"
else:
    userinput = userinput
    punct = ""


def string_split(userinput):
    for word in userinput:
        word = userinput.split(' ')
    return word

def reverse_string():
    global rev_lst
    for rev_lst in string_split(userinput):
        rev_lst = string_split(userinput)[::-1]
        rev_lst = (" ").join(rev_lst)
    if punct != "":
        print(punct,rev_lst)
    else:
        print(rev_lst)


string_split(userinput)
reverse_string()