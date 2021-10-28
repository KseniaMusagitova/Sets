rainbow_colors = {'red', 'orange', 'yellow', 'green' 'blue',}
print(rainbow_colors)
print(type(rainbow_colors))

empty_set = {}
print(empty_set)
print(type(empty_set))

empty_set = set()
print(type(empty_set))

number_list = [1, 42, 56, 3, 3, 3]
text_tuple = ('ddsdf', 'sdfsd', 'sdfs', 'hi', 'hi', 'hi')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)
print(set_from_list)
print(set_from_tuple)

set_from_list.add(777)
set_from_tuple.add('hello')
print(set_from_list)
print(set_from_tuple)

# удаление
set_from_list.pop()
print(set_from_list)
set_from_list.remove(3)
print(set_from_list)
set_from_list.discard(42)
print(set_from_list)
set_from_list.clear()
print(set_from_list)

# пример
text = set('Я ''изучаю ''Python')
print(text)
print(type(text))
