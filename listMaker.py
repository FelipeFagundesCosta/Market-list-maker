toBeDone = list(map(str, input('What do you plan on cooking this week? ').split(',')))

with open('./Files/Recepies.csv','r') as recepies:
    lista = list(map(str,recepies.read().split('\n')))

with open('./Files/Measures/liquids.txt','r') as liquids:
    liquids = list(map(str, liquids.read().split('\n')))
    
with open('./Files/Measures/solids.txt','r') as solids:
    solids = list(map(str, solids.read().split('\n')))
    
with open('./Files/Measures/units.txt','r') as units:
    units = list(map(str, units.read().split('\n')))
       
ingredients = []
reDo = True
while reDo:
    for i in range(len(toBeDone)):
        reDo = False
        found = False
        for j in range(len(lista)):
            realList = list(lista[j].split(';'))
            if toBeDone[i] in realList:
                food = realList[0]
                for k in range(1,len(realList)):
                    item = list(realList[k].split(':'))
                    item[1] = int(item[1])
                    ingredients.append(item)
                    found = True
        if not found:
            while not found:
                    print(f'\nThe recepie "{toBeDone[i]}" is not in our data base.')
                    print('To add a new recepie, ater the file "Recepies.csv"')
                    error = input(f'\nWould you like to rewrite "{toBeDone[i]}"? ').lower()
                    if error in 'simsmyesys':
                        correction = input('\nType the name of the recepie again: ').lower()
                        toBeDone[i] = correction
                        for l in range(len(lista)):
                            search = list(lista[l].split(','))
                            if correction in search[0]:
                                found = True
                                reDo = True
                                break
                    else:
                        found = True
            break

fixing = {}

for i in range(len(ingredients)):
    if ingredients[i][0] not in fixing:
        fixing[ingredients[i][0]] = ingredients[i][1]
    else:
        fixing[ingredients[i][0]] += ingredients[i][1]
                       
with open('List.csv', 'w') as lista:
    for i in fixing:
        if i in liquids:
            measure = 'ml'
        elif i in solids:
            measure = 'g'
        else:
            measure = 'un'
        lista.write(f'{i};{fixing[i]}{measure}\n')