# -*- coding: utf-8 -*-
"""homework1_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x3_4I9bbNw4vgopl7UnxmofntiU4jp1C
"""

# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
import random as r

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 


# Решение
# Пункт A
# генерируем случайные песни и их длины
rand_song1 = r.choice(my_favorite_songs)
rand_song2 = r.choice(my_favorite_songs)
rand_song3 = r.choice(my_favorite_songs)
# посмотрим на них
print(rand_song1)
print(rand_song2)
print(rand_song3)
# длины песен - элементы с индексом [1], сложим их
three_songs_length = rand_song1[1] + rand_song2[1] + rand_song3[1]
print (f'Три песни звучат {three_songs_length} минут')

# Пункт B
# теперь со словарём

# создаём список значений словаря
songs_length = list(my_favorite_songs_dict.values())
# выведем его
print(songs_length)
# выбираем три рандомных значения, складываем и выводим
rand_song_1_length = r.choice(songs_length)
rand_song_2_length = r.choice(songs_length)
rand_song_3_length = r.choice(songs_length)
three_songs_length = rand_song_1_length + rand_song_2_length + rand_song_3_length
print (f'Три песни звучат {three_songs_length} минут')

# таки пункт С
# Сгенерируйте случайные песни с помощью модуля random
# для списка:
# с помощью метода choice() выбираем список из случайной песни и длины песни
rand_song = r.choice(my_favorite_songs)
# выводим нулевой элемент для списка
# получается случайная песня
print(rand_song[0])

# для словаря:
# извлекаем в список ключи словаря
songs = list(my_favorite_songs_dict.keys())
# с помощью метода choice() выбираем песню
print(r.choice(songs))

# Пункт D
# Переведите минуты и секунды в формат времени. Используйте модуль datetime
import datetime as dt
# проитерируем все песенки
for song in my_favorite_songs:
    # время в формате float переведём в строку
    time_in_float = str(song[1])
    # разделим каждую получившуюся строку на до точки и после точки
    time = time_in_float.split('.')
    # запишем длину песни в формате времени: минуты - значения time_in_float до
    # точки, секунды - значения после точки
    song_time = dt.time(minute = int(time[0]),second = int(time[1]))
    # каждый элемент с индексом [1] в каждом списке общего списка
    # заменим на значение длины песни в формате времени
    song[1] = str(song_time)
# вот, что получилось
print(my_favorite_songs)

# для словаря:
# не получается пока что

