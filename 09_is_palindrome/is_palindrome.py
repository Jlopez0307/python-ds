def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    
    lower_case_phrase = phrase.lower()
    phrase_no_spaces = lower_case_phrase.replace(" ", "")
    print(phrase_no_spaces)
    print(phrase_no_spaces[::-1])

    

    if phrase_no_spaces == phrase_no_spaces[::-1]:
        return True
    elif phrase_no_spaces != phrase_no_spaces[::-1]:
        return False
