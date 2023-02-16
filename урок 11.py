'''Создайте функцию, которая принимает в качестве параметра - натуральное целое число.
Данная функция находит факториал полученного числа
Например, факториал числа 3 это число 6.
Теперь создайте список факториалов чисел от получившегося ранее факториала 6, до 1.
В итоге, на вход программа получает например число 3, возвращает число 6 (факториал числа 3) и вам нужно сделать список из факториалов 
числа 6 в убывающем порядке. Находим факториал числа 6 - это 720, затем от числа 5 - это 120 и так далее вплоть до 1
То есть, результирующий список будет выглядеть в нашем примере так:
[720, 120, 24, 6, 2, 1]'''

def factorial(number):
    result = 1
    for i in range(2, (number + 1)):
        result *= i
    return result


list_factorial = list()
n = int(input('Введите любое натуральное число: ', ))
source_factorial = factorial(n)
for e in range (source_factorial, 0, -1):
    list_factorial.append(factorial(e)) 
print(list_factorial)

#ЗАДАЧА 2
pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        },
    # и так далее
}


def create():
    last = collections.deque(pets, maxlen=1)[0]
    name = input('Введите имя питомца: ', )
    pets[last + 1] = {
                name: {
                    'Вид питомца': input('Введите вид животного: ', ),
                    'Возраст питомца': int(input ('Введите возраст животного (полных лет): ', )), 
                    'Имя владельца': input('Введите имя владельца: ', )
                }
            }
    return pets[last + 1]
    

def read(ID):
    if ID in pets:
        for key in pets[ID]:
            name = key
        age = 0
        vid = 0
        host_name = 0
        for key, value in pets[ID][name].items():
            if key == 'Вид питомца':
                vid = value 
            if key == 'Имя владельца':
                host_name = value 
            if key == 'Возраст питомца':
                age = value
                get_suffix(age)
        return (f'Это {vid} по кличке {name}. Возраст питомца: {get_suffix(age)}. Имя владельца: {host_name}')
    else:
        return ("Элемент не найден")


def update(ID):
    if ID in pets:
        name = input('Введите новое имя питомца: ', )
        pets[ID] = {
                    name: {
                        'Вид питомца': input('Введите вид нового животного: ', ),
                        'Возраст питомца': int(input ('Введите возраст животного (полных лет): ', )), 
                        'Имя владельца': input('Введите имя владельца: ', )
                    }
                }
        return pets[ID]
    else:
        print("Элемент не найден")


def delete():
    ID = int(input('Введите номер животного удаляемого из базы: ', ))
    if ID in pets:
        del pets[ID]
        print(f"Элемент под номером {ID} удален")
    else:
        print("Элемент не найден")
    return pets


def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False


def get_suffix(age):
    k = (age // 10 % 10 != 1) * age % 10
    g = {1: ' год', 2: ' года', 3: ' года', 4: ' года'}.get(k, ' лет')
    age = str(age) + g
    return age


def pets_list():
    for ID in pets:
        print(f"№ {ID} - {read(ID)} ")


import collections
command = 0
while command != 'stop':
    command = input('Введите команду: ', )
    if command == 'delete':
        delete()
    if command == 'update':
        ID = int(input('Введите номер животного в списке базы, данные которого нужно изменить: ', ))
        update(ID)
    if command == 'read':
        ID = int(input('Введите номер из базы интересующего Вас животного: ', ))
        print(read(ID))
    if command == 'create':
        create()
    if command == 'get_pet':
        ID = int(input('Введите номер из базы интересующего Вас животного: ', ))
        print(get_pet(ID))
    if command == 'pets_list':
        pets_list()
