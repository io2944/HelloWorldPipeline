import random

niveau = input('Veuillez saisir un niveau Facile:f, Moyen:m, Difficile:d ')
if niveau == 'f':
    nb_a_deviner = random.randint(0,10)
elif niveau == 'm':
    nb_a_deviner = random.randint(0,100)
else: nb_a_deviner = random.randint(0,1000)

essais = 1

repeter = True
while repeter:
    nb_choisi = int(input('Veuillez saisir un nombre: '))
    if nb_a_deviner < nb_choisi :
        print('Trop grand ')
    elif nb_choisi < nb_a_deviner :
        print('trop petit')
    else : 
        print('Succes!!! Le nombre etait :', nb_choisi, ' en ', essais, 'essai.s')
        repeter = False
    essais +=1
