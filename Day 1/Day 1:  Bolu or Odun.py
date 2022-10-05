def BoO(word: str) -> None:
    """Checks if a word contains special characters or a space."""

    special_chars= '''!()-[]{};:'"\,<>./?@#$%^&*~  '''

    if (type(word) != str) or (special_chars in word) or (' ' in word):
        print('Please remove all spaces or special characters')

    elif word.lower() in ['bolu', 'odun']:
        print(f'Welcome back, {word.title()}')

    else:
        print(f'It is nice to meet you, {word.title()}')

#Tests
BoO('Micheal Jackson')
BoO('Micheal')
BoO('Bolu')