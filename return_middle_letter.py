''' Return middle letter in a word, if the word has odd length or return the two middle words if even.'''

word="A"

def get_middle(word):
    return(word[(len(word)//2-1):(len(word)//2)+1] if len(word) % 2 == 0 else word[len(word)//2])

