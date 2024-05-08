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
from random import randint
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

'''функция формирования списка продуктов и их количества в расчете на указанное кол-во персон
    Должен быть следующий результат:
{
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}'''
def get_shop_list_by_dishes(dishes, person_count):
    print(f'Заказанные блюда: {random_order_dishes} на количество персон: {cnt_person}')
    print()
    list_to_prepare = {} #создаем словарь и будем помещаь в него список ингредиентов
    measure_and_quantity = {} #отдельный словарь, чтобы привести вывод результата {'measure': 'шт', 'quantity': 4}, где measure уже стоит на первом месте
    quantity = 0 # переменная кол-ва требуемых продуктов
    for dish in dishes: #для каждого блюда из списка заказанных блюд
        for product in cook_book[dish]: #берем словарь продукт
            if product['ingredient'] in list_to_prepare: #проверяем наличие продукта в новом словаре
                #если продукт в новом словаре существует, то обращаемся к его количеству и умножаем на кол-во персон
                quantity_next = int(product['quantity']) * person_count #новая переменная, для текущего выбранного продукта
                #к уже имеющемуся кол-ву для найденного продукта прибавляем найденное для текущего продукта
                list_to_prepare[product['ingredient']]['quantity'] = int(list_to_prepare[product['ingredient']]['quantity'])+int(quantity_next)
            else: #если продукта в новом словаре не существует, то обращаемся к его количеству и умножаем на кол-во персон
                quantity = int(product['quantity']) * person_count
            it = list(product.items()) #преобразуем наш словарь продукт-ед изм-кол-во в списко с кортежем
            measure = it[2] #возвращаем единицу измерения
            QNT = it[1] #возврщаем кол-во
            #производим перестановку элементов, сначала добавляем единицу измерения, затем кол-во
            measure_and_quantity = {measure[0]:measure[1]}
            measure_and_quantity.setdefault(QNT[0],quantity)
            list_to_prepare.setdefault(product['ingredient'],measure_and_quantity) #формируем результат, добавляя продукт, ед изменерия и пересчитанное кол-во в зависимости от кол-ва персон
    pprint(list_to_prepare)

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
                dish_name = recipe[0] #получаем название блюда
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
        #print(cook_book)

#небольшой код для получения случайного заказа из полученных блюд и количества персон
keys = list(cook_book.keys()) #получаем список ключей полученного словаря
cnt_person = randint(1,4) #случайное число персон от 1 до 4
cnt_dish = randint(1,4) #случайное число блюд от 1 до 4
random_order_dishes = [] #создаем случайный список выбранных блюд
for i in range(cnt_dish): #заполняем список
    random_order_dishes.append(keys[i])

get_shop_list_by_dishes(random_order_dishes,cnt_person) #вызываем функцию подсчета ингредиентов в расчете на персон, где cnt_person - случайное кол-во персон,random_order_dishes - случайный выбор блюд