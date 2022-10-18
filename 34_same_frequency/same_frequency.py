from typing import Counter


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_count = Counter(str(abs(num1)))
    num2_count = Counter(str(abs(num2)))

    if num1_count == num2_count:
        return True
    else:
        return False

    

    
    