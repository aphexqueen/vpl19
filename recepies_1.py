import re

with open ('Дашины рецепты.txt') as file:
    recepies = file.read()

names =re.findall(r'\d\. (.+)\. Ингредиенты:',recepies) # записать названия рецептов
text = re.findall(r'приготовления: (.+)',recepies)
recepies = recepies.lower()
list= re.findall(r'ингредиенты: (.+)\. этапы',recepies)  # список ингредиентов (1 элемент - все ингредиенты одного рецепта)

ings = []
for a in list:
    a = a.split(', ')
    ings.append(a) #список из подсписков; 1 подсписок - ингредиенты для одного блюда

print ('\nВас приветствует программа подбора рецепта по ингредиентам или коротко ПРОР\n')

have = input('Какие ингредиенты у тебя есть?\n')
if '.' in have:
    have= have.replace('.','')
have=have.lower().split(', ')

coinc = 0 # старт для отсчета количества совпадений по 1 рецепту
for ing in ings: 
    amount = len(ing) 
    
    for prod in have: 
        if prod in ing: 
            coinc+=1
    
    
    if amount - coinc <=2: 
        num = ings.index (ing)            
        print('\n/////       Приготовь следующий рецепт: ',names [num],'.\n') 
        if amount - coinc ==0:
            print('У тебя есть все продукты для этого рецепта! Открывай скорее кулинарную книгу! :)\n')
            if '.' in text[num]:
                text[num] = text[num].replace('.','.\n')
            print(text[num],'\n')
        else:    
            to_cook= ings[num]
            
            for i in have:
                for el in to_cook:
                    if el == i:
                        num1 = to_cook.index(el)
                        del to_cook [num1]
                        buy=', '.join(to_cook)
                        buy = buy+'.'
                        
            print ('Прости тебе не хватает некоторых ингредиентов.\nСходи в магазин, чтобы купить: ',buy,'\n')
            if '.' in text[num]:
                text[num] = text[num].replace('.','.\n')
            print ('Если ты все купил, лови рецепт \n',text[num],'\n \n Легкой готовки и Приятного аппетита!!!')
    coinc=0

    


    


