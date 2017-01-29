import re

def make_list(x):
    """ takes input x and breaks it down into a list of words """
    text = open(x).read().lower() # input text from nuance
    text = re.sub('[^a-z \n]', "", text)
    return (sorted(text.split()))

def compare(x, y):
    """ compares input with the target words """
    list_in = make_list(x)
    list_target = make_list(y)
    list_count = []
    for i in range (len(list_target)):
        x = 0
        for j in range (len(list_in)):
            if (list_in[j] == list_target[i]):
                x+=1
        list_count.append(x)
        x = 0
    for i in range (len(list_count)):
        print(list_target[i], list_count[i]) # prints each target word and the number of times it was used
