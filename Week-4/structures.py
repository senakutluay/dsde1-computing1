'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list". 

def first_and_last(the_list):
    """This function returns a list that contains the first and the last item of the given list"""
    newlist=[the_list[0],the_list[-1]]
    return newlist


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):
    if end<beginning:
        return ValueError
    newlist=the_list[beginning:end]
    newlistfinal=newlist[::-1]
    return newlistfinal


# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    a=the_list[index]
    multiply=3*a
    addition=list(str(multiply))
    firsthalf=the_list[0:index]
    lasthalf=the_list[(index+1)::]
    for c in addition:
        firsthalf.append(c)
    
    finallist= firsthalf + lasthalf
    return finallist
   


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    reverse_word=word[::-1]

    return bool(reverse_word == word)

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    lower=sentence.lower()
    nowhitespace= lower.replace(" ", "")
    
    punctuations = list('''!()-[]{};:'",<>./?@#$%^&*_~+''')
  
    for x in nowhitespace: 
        if x in punctuations: 
            nowhitespace = nowhitespace.replace(x, "")
    reverse_sentence=nowhitespace[::-1]
    return bool(reverse_sentence==nowhitespace)


# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentenece1, sentence2):
    sentence1new= sentenece1.strip()
    sentence2new= sentence2.strip()
    acceptable_ending=["?","!","."]
    if (sentence1new[0].isupper() == True) and (sentence2new[0].isupper() == True):
        if (sentence1new[-1] in acceptable_ending) and (sentence2new[-1] in acceptable_ending):
            return sentence1new + " " + sentence2new
        else:
            return 
    else:
        return 
    
        
# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False
    

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    if value in dictionary.values():
        return True
    else:
        return False





# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1,dictionary2):
    diction={**dictionary1, **dictionary2}
    return diction
