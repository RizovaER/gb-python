# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [10, None, -30, 'True', True, 9.5]


def my_type(element):
    for element in range(len(my_list)):
        print(type(my_list[element]))
    return


my_type(my_list)




# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

element_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
element = 0
while i < element_count:
    my_list.append(input("Введите значение списка "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[element], my_list[element + 1] = my_list [element + 1], my_list[element]
        element += 2
print(my_list)

# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите месяц по номеру "))
if month ==12 or month == 1 or month == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
        print("Такого месяца не существует")

# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

my_string = input("введите предложение ")
my_word = []
number = 1
for element in range(my_string.count(' ') + 1):
    my_word = my_string.split()
    if len(str(my_word)) <= 10:
        print(f" {number} {my_word [element]}")
        number += 1
    else:
        print(f" {number} {my_word [element] [0:10]}")
        number += 1

# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [5, 4, 3, 2, 1]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (000 - выход) "))
while digit != 000:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число (000 - выход) "))

    # *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
    # Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
    # (характеристиками товара: название, цена, количество, единица измерения).
    # Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
    # Пример готовой структуры:
    # [
     #    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
       #  (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
       # (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
   # ]
    # Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
    # например название, а значение — список значений-характеристик, например список названий товаров.
    # Пример:
    # {
     #    “название”: [“компьютер”, “принтер”, “сканер”],
       #  “цена”: [20000, 6000, 2000],
        # “количество”: [5, 2, 7],
        # “ед”: [“шт.”]
    # }'''

    goods = []
    while input("Would you like add product? Enter yes/no: ") == 'yes':
        number = int(input("Enter product number: "))
        features = {}
        while input("Would you like add product parameters? Enter yes/no: ") == 'yes':
            feature_key = input("Enter feature product: ")
            feature_value = input("Enter feature value product: ")
            features[feature_key] = feature_value
        goods.append(tuple([number, features]))
    print(goods)
    # goods = [(1, {'name': 'comp', 'price': '11'}), (2, {'name': 'pri', 'price': '22'})]
    analitics = {}
    for good in goods:
        for feature_key, feature_value in good[1].items():
            if feature_key in analitics:
                analitics[feature_key].append(feature_value)
            else:
                analitics[feature_key] = [feature_value]
    print(analitics)