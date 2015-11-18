infile = open("piglatin1.in","r")
outfile = open("piglatin1.out","w")

VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
s = infile.read()
s = s.strip('\n')

def convert_word(word):
    first_letter = word[0]
    if first_letter in VOWELS:  # if word starts with a vowel...
        return word + "yay"     # then keep it as it is and add hay to the end
    else:
        return word[1:] + word[:1] + "ay"    # like the lab mentions, word[1:]
                                            # returns the word except word[0]

def convert_sentence(sentence):
    list_of_words = sentence.split(' ')
    new_sentence = ""   # we'll keep concatenating words to this...
    for word in list_of_words:
        new_sentence = new_sentence + convert_word(word)    # ...like this
        new_sentence = new_sentence + " "   # but don't forget the space!
    return new_sentence

output = convert_sentence(s)
output = output[:-1] + "\n"
outfile.write(output)
