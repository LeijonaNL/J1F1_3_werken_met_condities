# sollicitatie.py

# Gender


gender = input('Wat is uw geslacht? ').lower()
print('U heeft ' + str(gender) + ' geantwoord.')


# Vraag 1

ervaringA = 0
ervaringB = 0
ervaringC = 0

repeat = True
while repeat:
    repeat = False
    ervaring = input('''Heeft U enkele jaren ervaring met: dierendressuur,
    jongleren of acrobatiek?
    Voor dierendressuur, vul in "A".
    Voor jongleren, vul in "B"
    Voor acrobatiek, vul in "C"
    Heeft U in geen van deze onderwerpen ervaring? vul dan in "Nee" ''').lower()
    if ervaring == 'a':
        ervaringA = int(input('''U heeft dierendressuur geselecteerd, 
        hoeveel jaren ervaring heeft U hierin? '''))
        print('U heeft aangegeven dat U ' + str(ervaringA) + 
        ' jaren ervaring heeft in dierendressuur, U gaat nu door naar de volgende vraag.')
    elif ervaring == 'b':
        ervaringB = int(input('''U heeft jongleren geselecteerd,
        hoeveel jaren ervaring heeft U hierin? '''))
        print('U heeft aangegeven dat U ' + str(ervaringB) + 
        ' jaren ervaring heeft in jongleren, U gaat nu door naar de volgende vraag.')
    elif ervaring == 'c':
        ervaringC = int(input('''U heeft acrobatiek geselecteerd, 
        hoeveel jaren ervaring heeft U hierin? '''))
        print('U heeft aangegeven dat U ' + str(ervaringC) + 
        ' jaren ervaring heeft in acrobatiek, U gaat nu door naar de volgende vraag.')
    elif ervaring == 'nee':
        print('''U heeft geen ervaring geselecteerd, 
        U gaat nu door naar de volgende vraag.''')
    else:
        print('Dat is geen mogelijk antwoord')
        repeat =  True

if ervaringA >= 4:
    requirement1 = True
elif ervaringB >= 5:
    requirement1 = True
elif ervaringC >= 3:
    requirement1 = True
else:
    requirement1 = False


# Vraag 2

repeat = True
while repeat:
    repeat = False
    diploma = input('Bent U in bezit van een diploma in MBO-4 ondernemen of hoger? '
    ' Antwoord met "Ja" of "Nee". ').lower()
    if diploma == 'ja':
        print('U hebt aangegeven dat U in bezit bent van een diploma MBO-4 ondernemen.'
        ' U gaat nu door naar de volgende vraag.')
    elif diploma == 'nee':
        print('U hebt aangegeven dat U niet in bezit bent van een diploma MBO-4 ondernemen.'
        ' U gaat nu door naar de volgende vraag.')
    else:
        print('Dat is geen mogelijk antwoord.')
        repeat = True
    
if diploma == 'ja':
    requirement2 = True
elif diploma == 'nee':
    requirement2 = False


# Vraag 3

repeat = True
while repeat:
    repeat = False
    rijbewijs = input('Heeft U een geldig vrachtwagen rijbewijs tot Uw beschikking?'
    ' Antwoord met "Ja" of "Nee". ').lower()
    if rijbewijs == 'ja':
        print('U hebt aangegeven dat U in bezit bent van een geldig vrachtwagen rijbewijs.'
        ' U gaat nu door naar de volgende vraag. ')
    elif rijbewijs == 'nee':
        print('U hebt aangegeven dat U niet in bezit bent van een geldig vrachtwagen rijbewijs.'
        ' U gaat nu door naar de volgende vraag. ')
    else:
        print('Dat is geen mogelijk antwoord. ')
        repeat = True

if rijbewijs == 'ja':
    requirement3 = True
elif rijbewijs == 'nee':
    requirement3 = False


# Vraag 4

repeat = True
while repeat:
    repeat = False
    hoed = input('Bent U in bezit van een hoge hoed?'
    ' Antwoord met "Ja" of "Nee" ').lower()
    if hoed == 'ja':
        print('U hebt aangegeven dat U in bezit bent van een hoge hoed.'
        ' U gaat nu door naar de volgende vraag. ')
    elif hoed == 'nee':
        print('U hebt aangegeven dat U niet in bezit bent van een hoge hoed.'
        ' U gaat nu door naar de volgende vraag. ')
    else:
        print('Dat is geen mogelijk antwoord.')
        repeat = True

if hoed == 'ja':
    requirement4 = True
elif hoed == 'nee':
    requirement4 = False


# Vraag 5

snorB = 0
krulhaarL = 0

repeat = True
while repeat:
    repeat = False
    if gender == 'man':
        snor = input('Heeft U een snor?'
        ' Antwoord met "Ja" of "Nee". ').lower()
        if snor == 'ja':
            snorB = int(input('Hoe breed is uw snor in centimeters?'
            ' Antwoord alleen met een afgerond getal. '))
            print('U hebt aangegeven dat U een snor hebt die ten minste ' + str(snorB) + 
            ' centimeter breed is. '
            ' U gaat nu door naar de volgende vraag. ')
        elif snor == 'nee':
            print('U hebt aangegeven dat U geen snor hebt.'
            ' U gaat nu door naar de volgende vraag.')
        else:
            print('Dat is geen mogelijk antwoord.')
            repeat = True
    elif gender == 'vrouw':
        krulhaar = input('Heeft U rood krulhaar?'
        ' Antwoord met "Ja" of "Nee". ').lower()
        if krulhaar == 'ja':
            krulhaarL = int(input('Hoe lang is Uw haar in centimeters?'
            ' Antwoord alleen met een afgerond getal. '))
            print('U hebt aangegeven dat U rood krulhaar hebt dat ten minste ' + str(krulhaarL) + 
            ' lang is.'
            ' U gaat nu door naar de volgende vraag. ')
        elif krulhaar == 'nee':
            print('U hebt aangegeven dat U geen rood krulhaar hebt.'
            ' U gaat nu door naar de volgende vraag.')
        else:
            print('Dat is geen mogelijk antwoord.')
            repeat = True

if snorB >= 10:
    requirement5 = True
elif krulhaarL >= 20:
    requirement5 = True
else:
    requirement5 = False


# Vraag 6

lengte = 0

repeat = True
while repeat:
    repeat = False
    lengte = int(input('Hoe lang bent U in centimeters?'
    ' Antwoord alleen met een afgerond getal. '))
    print('U hebt aangegeven dat U ongeveer ' + str(lengte) + 'cm lang bent.'
    ' U gaat nu door naar de volgende vraag.')

if lengte >= 150:
    requirement6 = True
else:
    requirement6 = False


# Vraag 7

gewicht = 0

repeat = True
while repeat:
    repeat = False
    gewicht = int(input('Wat is Uw gewicht in kg?'
    ' Antwoord alleen met een afgerond getal. '))
    print('U hebt aangegeven dat U ongeveer ' + str(gewicht) + 'kg weegt.'
    ' U gaat nu door naar de volgende vraag.')

if gewicht >= 90:
    requirement7 = True
else:
    requirement7 = False


# Vraag 8


repeat = True
while repeat:
    repeat = False
    certificaat = input('Bent U in bezit van een certificaat "Overleven met gevaarlijk personeel"?'
    ' Antwoord met "Ja" of "Nee". ').lower()
    if certificaat == 'ja':
        print('''U hebt aangegeven dat U in bezit bent van een certificaat
        "Overleven met gevaarlijk personeel".''')
    elif certificaat == 'nee':
        print('''U hebt aangegeven dat U niet in bezit bent van een certificaat
        "Overleven met gevaarlijk personeel".''')
    else:
        print('Dat is geen mogelijk antwoord.')
        repeat = True

if certificaat == 'ja':
    requirement8 = True
else:
    requirement8 = False


# Resultaat

if (requirement1 and requirement2 and requirement3 and requirement4 and \
requirement5 and requirement6 and requirement7 and requirement8):
    print('Gefeliciteerd! U bent aangenomen!')
else:
    print('Jammer, U bent niet aangenomen.')
