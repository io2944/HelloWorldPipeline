number = int(input('Choisisez un nombre: '))

list_multiples = []

for i in range(1, 11):
    if i%3 == 0:
        list_multiples.append(str(i*number) + '*')
    else: list_multiples.append(i*number)

print(list_multiples)