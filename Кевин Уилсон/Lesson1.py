import pickle

num1 = 2
num2 = 3
print("num1 + num2 = ", num1 + num2)

# List - Список mutable
# упорядоченная (order) структура данных
shopping_list = ['breed', 'milk', 'coffee', 5]
print(type(shopping_list))
print(shopping_list[3])
print(shopping_list)
shopping_list.append('cucumber')
shopping_list.insert(1, 'potatos')
shopping_list.remove('milk')
print(shopping_list)
shopping_list.pop(1)
print(shopping_list)

# Set- Набор или Множество mutable
# неупорядоченная (unorder) структура данных
names_set = {'denis', 'oleg', 'slavik', 'denis'}
varius_set = {1, 'bananas', 3.14, 24}
print(type(names_set))
print(names_set)
print(varius_set)
# если список инициализировать пустыми скобками то это будет СЛОВАРЬ!!!
test_set = {}
test1_set = set()
print(type(test_set))
print(test_set)
print(type(test1_set))
print(test1_set)

names_set.add('Petrovich')
print(names_set)
names_set.remove('denis')
print(names_set)

# Tuple- Кортеж imutable
# неупорядоченный
user = (1, 'Denis', '12345')
print(user)
print(type(user))
print(f'ID = {user[0]} User = {user[1]} Password = {user[2]}')

# Dict - Словарь
capitalCities = {
    'UK': 'London',
    'Australia': 'Canberra',
    'USA': 'Washington DC',
    'Spain': 'Madrid'
}

print(capitalCities)
print(type(capitalCities))

print(capitalCities['Australia'])

for key in capitalCities:
    print(f'Столица {key} это {capitalCities[key]}')

capitalCities.update({'France': 'Paris'})

for key in capitalCities:
    print(f'Столица {key} это {capitalCities[key]}')

#num = input('Введи число: ')
num = int(input('Введи число: '))
print(num)
print(type(num))

file = open('data.txt', 'a')
file.write('Эта срока добавлена в файл')
file.close()

file = open('data.txt', 'r')
text = file.read()
print(f'Вот что мы прочитали из файла: {text}')
file.close()

file = open('binary.dat', 'wb')
pickle.dump('Эта строка записана побитово', file)
file.close()

file = open('binary.dat', 'rb')
data = pickle.load(file)
print(data)
file.close()

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
res = factorial(4)
print(res)