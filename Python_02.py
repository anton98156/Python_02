# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# import os
# os.system("clear")

# num = float(input("Введите число: "))

# def result(num):
#     sum = int(0)
#     for i in str(num):
#         if i != ".":
#             sum = sum + int(i)
#     return sum

# print(f"Сумма цифр числа = {result(num)}")
    
# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# import os
# os.system("clear")

# n = int(input("Введите число: "))

# def factorial(n):
# 	if n == 1:
# 		return 1
# 	else:
# 		return n * factorial(n - 1)

# list = []
# for e in range(1, n + 1):
#     list.append(factorial(e))

# print(f"{list}")

# 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# Пример: для n = 6: [2, 2.25, 2.37, 2.441, 2.488, 2.522].

# import os
# os.system("clear")

# n = int(input("Введите N: "))

# list = []
# for n in range (1, n + 1):
#     list.append(round((1+1/n)**n, 3))
# print(f"{list}")

# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import os
os.system("clear")

n = int(input("Введите число: "))

list = []
for n in range (-n, n + 1):
    list.append(n)
    
print(f"{list}")
# В связи с тем, что file.txt не был прикреплен на платформе, позиции не были извевстны, поэтому выбрал случайные
print(f"Произведение элементов = {list[6] * list[7]}")


# 5 Реализуйте алгоритм перемешивания списка.

# import os
# os.system("clear")
