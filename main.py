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
