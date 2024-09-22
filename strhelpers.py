from random import shuffle as l_shuffle

def reverse(str_value):
    return str_value[::-1]

def str_shuffle(str_value):
    str_list = list(str_value) #needs to convert to a list for it to work
    l_shuffle(str_list)
    return "".join(str_list) #convert back to a string