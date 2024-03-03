def print_upper_words(words):
    """Print each word on seperate line, but all uppercased.

        >>> print_upper_words(["Python", "is", "the", "best"])
        Should print:

        PYTHON
        IS
        THE
        BEST
    """

    for word in words: #forloop for words parameter
        print(word.upper()) #upper function for print

print_upper_words(["Python", "is", "the", "best"])


def print_upper_words2(words):
    """Print each word on seperate line, uppercased, only if starts with E or e.

        >>> print_upper_words2(["Event", "everyone", "Randy"])
        Should print:

        EVENT
        EVERYONE
    """

    for word in words: #forloop for words parameter
        if word.startswith("e") or word.startswith("E"): #startwith function for print
            print(word.upper()) #changes words to upper case
    
print_upper_words2(["Event", "everyone", "Randy"])


def print_upper_words3(words, must_start_with):
    """Print each word on seperate line, uppercased, if starts with a letter given in must_start_with

        >>> print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],
        ...                   must_start_with=["h", "y"])
        Should print:

        HELLO
        HEY
        YO
        YES
    """

    for word in words: #for loop for words
        for letter in must_start_with: #for loop for must_start_with
            if word.startswith(letter): #if statement if words start with letter given
                print(word.upper()) #prints those words in uppercase
                break #breaks line

print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"], must_start_with=["h", "y"])
