'''
Write a function that takes in a string of one or more words, and returns the same string,
but with all five or more letter words reversed (Just like the name of this Kata).
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
'''
sentence = "This is a wacky fabulous test"

def spin_words(sentence):
    sent_lst = sentence.split(" ")
    new_list = []
    for i in sent_lst:
        if len(i) >= 5:
            new_list.append(i[::-1])
        else:
            new_list.append(i)
    return " ".join(new_list)


print(spin_words(sentence))

'''
return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")]) #ONE LINE SOLUTION
'''





