'''должен получиться следующий словарь
cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }'''
from pprint import pprint

cook_book = {} #создаем словарь, где ключом будет название блюда, а значениями - значения списка ingredients
ingredients = [] #создаем список, где значениями будут словари с ключами ingredient_name, quantity и measure

'''функция создания рецепта recipe_creation которая будет принимать на вход список вида 
    ['Омлет', '3', 'Яйцо | 2 | шт', 'Молоко | 100 | мл', 'Помидор | 2 | шт'] 
    как название блюда и его игредиенты'''
def recipe_creation(recipe):
    #dish_name = recipe[0] #в переменную помещаем 0 элемент списка, который является названием блюда. Например, "Омлет"
    #cnt_ingredients = int(recipe[1])
    ingredients_list = recipe[2:] #срез списка, например 'Яйцо | 2 | шт', 'Молоко | 100 | мл', 'Помидор | 2 | шт'
    for i in ingredients_list: #для каждого элемента списка выполянем его разбивку по символу "|"
        list_of_ing = i.rstrip().split("|") #пример результата ['Яйцо ', ' 2 ', ' шт']
        dict_ingredients = ingredient_list_creation(list_of_ing) #помещаем результат выполения функции в переменную dict_ingredients, которая вернет нам словарь вида {'ingredient': 'Яйцо', 'quantity': '2', 'measure': 'шт'}
        ingredients.append(dict_ingredients) #добавляем в наш определенный список результат {'ingredient': 'Яйцо', 'quantity': '2', 'measure': 'шт'}, как отдельный элемент списка
        #cook_book.setdefault(dish_name,ingredients)  # добавляем в итоговый словарь по ключу dish_name список ingredients
        #cook_book = {dish_name:ingredients} #добавляем в итоговый словарь по ключу dish_name список ingredients
    return ingredients
    #print(cook_book) #выволим результат

'''функция формирования словаря ингредиентов для получения словаря вида {'ingredient': 'Яйцо', 'quantity': '2', 'measure': 'шт'}'''
def ingredient_list_creation(list_name): #в функцию передаем на вход список вида ['Яйцо ', ' 2 ', ' шт']
    #каждый список состоит из 3 элементов, поэтому создаем словарь и по ключам добавляем значения
    ingredient_name = {}
    ingredient_name.setdefault("ingredient",list_name[0].strip()) #ингредиент, из нашего примера это 'Яйцо'
    ingredient_name.setdefault("quantity", list_name[1].strip()) #количество, из нашего примера это '2'
    ingredient_name.setdefault("measure", list_name[2].strip()) #ед измерения, из нашего примера это 'шт'
    return ingredient_name #возвращаем результат

#открываем файл и преобразуем все строки в список
#в списке есть элемент '\n', до которого будем бежать и использовать для формирования отдельного списка- рецепта блюда
#краткая суть "нарезать" общий список на отдельные списки- рецепты и работать с отдельными списками- рецептами вытягивая и преобразовывая информацию
with open('recipes.txt', encoding='utf-8') as f: #открываем файл recipes.txt, кодировка UTF-8
    #while True: #бежим по строчкам пока не конец файла
        dish_name = f.readlines() #преобразуем файл в список, объединяя все данные в один список
        length = len(dish_name) #получаем длину списка
        recipe = [] #создаем новый список recipe, в который будем помещать рецепт отдельного блюда
        cnt_el = 0 #кол-во элементов списка равно 0 изначально
        for el in dish_name: # бежим по каждому элементу списка dish_name
            cnt_el += 1 #увеличиваем счетчик после отбора элемента списка
            if el == '\n' and cnt_el != length:  #будем отсекать каждый рецепт по элементу '\n' списка dish_name для получения списка вида ['Омлет', '3', 'Яйцо | 2 | шт', 'Молоко | 100 | мл', 'Помидор | 2 | шт']
                dish_name = recipe[0]
                recipe_creation(recipe) #как только список- рецепт блюда сформирован вызываем функцию для обработки ингредиентов и передаем в нее наш список вида ['Омлет', '3', 'Яйцо | 2 | шт', 'Молоко | 100 | мл', 'Помидор | 2 | шт']
                cook_book.setdefault(dish_name,ingredients)  # добавляем в итоговый словарь по ключу dish_name список ingredients
                recipe = [] #обнуляем список для следующего списка- рецепта
                ingredients = [] #обнуляем список ингредиентов
            elif cnt_el == length: #для того, чтобы зацепить последний элемент списка
                recipe.append(el.strip()) #добавляем этот последний элемент в список и вызываем функцию его обработки
                dish_name = recipe[0]
                recipe_creation(recipe) #как только список- рецепт блюда сформирован вызываем функцию для обработки ингредиентов и передаем в нее наш список вида ['Омлет', '3', 'Яйцо | 2 | шт', 'Молоко | 100 | мл', 'Помидор | 2 | шт']
                cook_book.setdefault(dish_name,ingredients)  # добавляем в итоговый словарь по ключу dish_name список ingredients
                recipe = [] #обнуляем список для следующего списка- рецепта
                ingredients = [] #обнуляем список ингредиентов
            else:
                recipe.append(el.strip()) #добавляем элемент из общего списка в список- рецепт приготовления блюда
        pprint(cook_book)