#!/usr/bin/lessons
# -*- coding: utf-8 -*-
import math
#__author__ = 'Ваши Ф.И.О.'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей lessons.


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4


def task1():
    x = input("x:")
    a = str(x)
    counter = 0
    #print (a)
    index = len(a) - 1
    while counter <= index:
        #print (a[counter])
        counter = counter+1
    print max(a)
    print ("finished")

def task2():
    a = input("a: ")
    b = input("b: ")
    a = a*b
    b = a/b
    a = a/b

    print ('a = ',a,'b = ',b)

def task3():
    a = input("a")
    b = input("b")
    c = input("c")
    d= (b*b)-4*(a*c)
    if d<0:
        print ("нет решения")
    elif d==0:
        x0=(-b)/2*a
        print ("есть один корень", x0)
    else:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        print ('x1', x1, 'x2', x2)

task3()
#task2()
#task3()
