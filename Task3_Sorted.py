import os, glob

f_res = open("merging.txt","w+",encoding = "UTF-8") #создаем результирующий файл, в который будем помещать данные из файлов с нумерацией строк

folder = os.path.join(os.getcwd(),'files') #мои файлы лежат в папке Files, получаем путь до нее
#print(folder)
cnt_file = 0 #счетчик открытых файлов
file_structure = {} #будет итоговым словарем, в котором будут ключами названия файлов, а значениями - словарь с ключами кол-во строк, текст и номер файла
file_data = {} #словарь, который бедт содержать информацию о наших файлах. Словарь с ключами кол-во строк, текст и номер файла и значениями для этих ключей
'''Функция подсчета строк в файле. В качестве параметра передаем ссылку на файл'''
def lines_calcualtion(f):
    test = f.readlines() #преобразуем содержимое файла в список
    return len(test)

for filename in glob.glob(f'{folder}/*.txt'):
    with open(filename, encoding="UTF-8") as f: #открываем файл по очереди
        cnt_file = cnt_file + 1 #счетчик кол-ва файлов
        file = filename.split('/') #разбиваем путь файла
        file_name_text = file[len(file)-1:][0] #получаем имя файла
        file_data = {'cnt_rows':lines_calcualtion(f)} #добавляем в словарь ключ cnt_rows и результат выполнения функции подсчета кол-ва строк в файле
        #f = open(filename, encoding="UTF-8")
        with open(filename, encoding="UTF-8") as f:
            file_data.update({'text':f.readlines()}) #обновляем словарь, добавляя в него еще один ключ text и текст файла в виде списка
            file_data.update({'file_number':cnt_file}) #обновляем словарь, добавляя в него еще один ключ file_number - номер подобранного файла по порядку
            file_structure.setdefault(file_name_text,file_data) #формируем наш полный словарь с данными в виде ключ- имя файла:значение- словарь с ключами cnt_rows и text - {file_name: {cnt_rows:value} {text:value}}
#далее нам нужно отсортировать наш словарь
#lkz
list_cnt_rows = [] #создаем список, в отрый будем помещать значения cnt_rows по ключу имя_файла
key_names = list(file_structure.keys()) #вытаскиваем все ключи словаря-струтуры
for file_name in key_names: #пробегаемся по ключам
    cnt_file_rows = file_structure[file_name]['cnt_rows'] #кладем в переменную кол-во строк
    list_cnt_rows.append(cnt_file_rows) #добавялям в списое кол-во строк
sorted_cnt_rows = sorted(list_cnt_rows) #сортируем список, коорый содержит все вытащенные кол-ва строк
#будем сопоставлять кол-во строк названию файла
for i in sorted_cnt_rows: #для каждого элемента списка кол-ва строк
    for file_name in key_names: #для каждого элемента списка ключей имен файлов
        if file_structure[file_name]['cnt_rows'] == i: #если количество строк совпадает для ключа имя-файла+кол-во строк
            f_res.write(file_name+'\n') #записываем имя файла в результрующий файл
            f_res.write(str(i)+'\n\n') #записываем кол-во строк в результрующий файл
            file_number = file_structure[file_name]['file_number']
            for index, value in enumerate(file_structure[file_name]['text']): #преобразуем список- текст файла в виде индекс элемента списка и его значение. Далее, для корректного вывода будем увеличивать значение индекса на 1
                f_res.write(f'Строка номер "{str(index+1)}" {value.strip()} файла номер "{file_number}", имя файла "{file_name}"\n') #преобразуем результат построчного вывода с нумерацией строк
    f_res.write('\n') #для читабельности добавляем перевод строки
f_res.close() #закрываем файл- результат
print("Обработка файлов завершена. Результат сохранен в файл 'MERGING.txt'", )