def palindrome(lista):
    result = list()
    for text in lista:
        if text[::-1] == text:
            print(True)
        else:
            print(False)
    return result

    """
    Check if the given word is a palindrome
    Arguments: list of words, str
    """
 
print(palindrome(["kajak", "sowa", "woda"]))
