from data import dictionary, letter_score

def load_words(dicco):
    """Load dictionary into a list and return list"""
    wordbook = open(dicco,"r")
    words = []
    for word in wordbook:
        word= ''.join(word.strip())
        words.append(word)
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    ans=0
    for letter in word:
        ans+=letter_score[letter]
    return ans

def max_word_value(*args):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    noArgs=True 
    for arg in args:
        words = load_words(arg)
        noArgs=False
    
    if noArgs:
        words = load_words(dictionary)
    
    maxval=0
    maxstring=""
    for word in words:
        val=calc_word_value(word)
        if val>maxval:
            maxval=val
            maxstring=word
    return maxstring


if __name__ == "__main__":
    pass