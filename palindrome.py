def palindrome(text):

    """
    Check if the given word is a palindrome
    Arguments: list of words, str

    """
    text = text.lower().replace(" ", "")
    return text == text[::-1] 
    

print(palindrome("Kobyła ma mały bok"))


