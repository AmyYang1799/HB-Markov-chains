"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    words.append(None)

    for i in range(len(words)-2):
        key = (words[i], words[i + 1])
        if key not in chains:
            chains[key] = []        #values list
        
        chains[key].append(words[i +2])


    return chains


def make_text(chains):
    """Return text from chains."""

    key = choice(list(chains.keys()))  #get starting key from list of keys
    words = [key[0],key[1]]             #starting words
    next_word = choice(chains[key])
    
    while next_word is not None:
        words.append(next_word) # add next_word to established list
        key = (key[1], next_word)   #find next key
        next_word = choice(chains[key])    #find new nextword
    
    return ' '.join(words)
    
    # for key, value in chains:
    #     key = choice([key])
    #     words.extend(list(key))
    #      = choice(chains[key])
    #     print(words)
    #     break
    #for 
        #words.append(next)
        #key = (words[1], next)
        #words.append(choice(chains[key]))
    
    #chains[(words[1], words[2])]

    # random_text = ' '.join(words)
    #print(words)

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
