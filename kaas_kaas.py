# Kaas, kaas en nog eens kaas


antwoord = input('Is de kaas geel? ')
if antwoord == 'ja':
    antwoord2 = input('Zitten er gaten in? ')
    if antwoord2 == 'ja':
        antwoord3 = input('Is de kaas belachelijk duur? ')
        if antwoord3 == 'ja':
            print('De goede kaas is de Emmenthaler.')
        else:
            print('De goede kaas is de Leerdammer.')
    else:
        antwoord4 = input('Is de kaas hard als steen? ')
        if antwoord4 == 'ja':
            print('De goede kaas is de Parmigiano Reggiano.')
        else:
            print('De goede kaas is de Goudse kaas.')
else:
    antwoord5 = input('Heeft de kaas blauwe schimmels? ')
    if antwoord5 == 'ja':
        antwoord6 = input('Heeft de kaas een korst? ')
        if antwoord6 == 'ja':
            print('De goede kaas is de Bleu de Rochbaron.')
        else:
            print('''De goede kaas is de Foume d'Ambert''')
    else:
        antwoord7 = input('Heeft de kaas een korst? ')
        if antwoord7 == 'ja':
            print('De goede kaas is de Camembert.')
        else:
            print('De goede kaas is de Mozzarella.')