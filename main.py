# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных свидетельствует пустая строка.
print("Задание 1")
user_write = input("Введите Ваше предложение ")
with open(r"D:\AI\text.txt", "a+") as file:
    file.write(f"{user_write}\n")
    file.seek(0)
    content = file.read()
    print(content)
# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
print("Задание 2")
with open(r"D:\AI\text1.txt", "r") as file1:
    content1 = file1.read()
    print(content1)
# 3  Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.
sure_name = input("Введите фамилию сотрудника ")
salary = input("Введите оклад сотрудника в руб.")
with open(r"D:\AI\dohod.txt", "a+") as file2:
    file2.write(f'{sure_name} {salary}\n')
    file2.seek(0)
    str = file2.read().splitlines()
    dict = {}
    for line in str:
        key, value = line.split(' ')
        dict.update({key: value})
    print(dict)
list_user = list()
for k, v in dict.items():
    if int(v) <= 20000:
        print(f"Фамилия: {k}, зарплата: {v}")
unit = 0
count = 0
result = 0
for k, v in dict.items():
    if int(v) <= 20000:
       count = count + 1
       unit = unit + int(v)
result = unit / count
print(f"Средняя зарплата сотавляет ", result)
#4. Создать (не программно) текстовый файл со следующим содержимым:
#4. One — 1
#4. Two — 2
#4. Three — 3
#4. Four — 4
print("Задание 4")
with open(r"D:\AI\text2.txt", "r", encoding="utf-8") as file4:
    text4 = file4.read()
    text4.replace("One", "Один")
    text4.replace("Two", "Два")
    text4.replace("Three", "Три")
    text4.replace("Four", "Четыре")
    print(text4)
# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.
print("Задание 5")
with open(r"D:\AI\text3.txt", "a+") as file6:
    file6.write("1 2 3 4 5 6 7 8 9")
    file6.seek(0)
    text6 = file6.read().split(" ")
    print(text6)
count_result = 0
for i in text6:
    count_result = count_result + int(i)
print(f"Сумма чисел равна {count_result}")
# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.
print("Задание 6")
with open(r"D:\AI\text4.txt", "r", encoding="utf-8") as file7:
    text7 = file7.read().splitlines()
    dict_lesson = {}
    for line in text7:
        key, value = line.split(": ")
        dict_lesson.update({key: value})
print(dict_lesson)
# 7 Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
print("Задание 7")
with open(r"D:\AI\text5.txt", "r", encoding="utf-8") as file8:
    text8 = file8.read().splitlines()
    dict_lesson1 = {}
    for line in text8:
        key = line.split(" ")[0]
        value = line.split(" ")[2]
        value2 = line.split(" ")[3]
        value_total = int(value) - int(value2)
        dict_lesson1.update({key: value_total})
print(dict_lesson1)
count_dict = 0
count_total = 0
for key, value in dict_lesson1.items():
    count_dict = value + count_dict
    count_total = count_total + 1
count_result = count_dict / count_total
average_dict = {}
average_dict.update({"average_profit": count_result})
list_firm = list()
list_firm.append(dict_lesson1)
list_firm.append(average_dict)
print(list_firm)
list_json = list_firm.__str__()
with open(r"D:\AI\text4.json", "w", encoding="utf-8") as file_json:
    file_json.write(list_json)




