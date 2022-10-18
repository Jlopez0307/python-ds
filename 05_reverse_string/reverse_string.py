def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    # Uses slice notation, first two params are empty, and the third is used to reverse string
    return phrase[::-1]
