import sys
import xml.dom.minidom
import re
import tkinter


def treatment_path(path):
    path = path.replace("\\", "/")
    path = path.replace('"', "")
    result = re.findall('.xml$', path)
    if len(result) != 0:
        return path
    else:
        sys.exit("Вы ввели файл формата не XML")

def summ_poi(doc, poi):
    summa = 0
    summ_list = []
    doc = doc.getElementsByTagName('poi')
    for name in doc:
        if name.getAttribute("name") == f"{poi}":
            summ_list.append(name.getAttribute("duration"))
    for i in summ_list:
        if i != "":
            summa += float(i)
    return summa




print("Введите путь к файлу для поиска:")
#Обрабатываем вводимую ссылку к файлу
path = treatment_path(input())

#Парсим XML
doc = xml.dom.minidom.parse(f'{path}')
#Выбираем опции работы скрипта
print('Введите имя POI')
poi = input()
while poi != 0:
    print(summ_poi(doc, poi))
    print("Введите имя POI, если вам необходимо осуществить поиск длительности конкретного POI, \n0 - если хотите завершить работу скрипта")
    poi = input()





