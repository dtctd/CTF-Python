infile = open("piglatin2.in","r")
outfile = open("piglatin2.out","w")

lst = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
s = infile.read()
s = s.strip('\n')

def convert_word(word):
    first_letter = word[0]
    if first_letter in lst and word[-3:] == "yay" : 
        if (any(x.isupper() for x in word)):
            return word[:-3].lower().capitalize()
        else:
            return word[:-3]
    else:
        if (any(x.isupper() for x in word)):
            word = word[-3] + word[:-3]
            return word.lower().capitalize()
        else:
            return word[-3] + word[:-3]

def convert_sentence(sentence):
    list_of_words = sentence.split(' ')
    new_sentence = ""   
    for word in list_of_words:
        new_sentence = new_sentence + convert_word(word)    
        new_sentence = new_sentence + " "
    return new_sentence

output = convert_sentence(s)
output = output[:-1] + "\n"
outfile.write(output)
