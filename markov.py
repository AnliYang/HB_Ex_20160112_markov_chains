from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as list of strings.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path) as open_file:
        full_text = open_file.read()
        text_to_return = full_text.split()

    return text_to_return

def make_chains(text_list):
    """Takes input text as list of strings; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    # # your code goes here
    # with our list of strings (text_list), we'll use a for loop:
    #     (to create the keys:)
    #     for each index:
    #         create a tuple for the string at that index, string at index + 1
    #         set the value for that key to an empty list (to prep for next for loop)
    #         until the end of the list (set a limit of some sort)
    third_to_last_index = len(text_list) - 2

    for index in range(third_to_last_index):
        bigram_key = (text_list[index], text_list[index + 1])
        
        if chains.get(bigram_key):
            chains[bigram_key].append(text_list[index + 2])
        else:
            chains[bigram_key] = [text_list[index + 2],]

    # when we optimize, this chains setting will wipe out existing key: lists of strings

    #     (to set values to each key:)
    #     for each bigram in the text
    #         if it matches a key tuple:
    #             for that dictionary[key tuple], append to the values to list

    # for index in range(third_to_last_index):
    #     test_against_key = (text_list[index], text_list[index + 1])
    #     chains[test_against_key].append(text_list[index + 2])

    return chains


# make_chains(open_and_read_file("green-eggs.txt"))

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # generate random tuple key (using choice) to call
    # set variable random_text (list) to include the two strings from the tuple
    initial_key = choice(chains.keys())
    random_text = [initial_key[0], initial_key[1]]

    while True:
        
        current_key = (random_text[-2], random_text[-1])

        if chains.get(current_key):
    # with the random tuple, get a random string (using choice) 
    # from the tuple's value list and add that value to random_text
            next_word = choice(chains[current_key])
            random_text.append(next_word)

    # turn last two words of random_text into tuple like so 
    # (random_text[-2], random_text[-1])


        else:
            break

    # repeat process from above

    random_text[0] = random_text[0].title()
    text = ' '.join(random_text)

    return text



input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
