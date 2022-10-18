def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    phraseDict = dict()

    for char in phrase:

        if char not in phraseDict:
            phraseDict[char] = 1

        else: 
            phraseDict[char] = phraseDict[char] + 1
    
    return phraseDict