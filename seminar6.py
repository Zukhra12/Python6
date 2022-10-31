#Задача 1
#Задайте список из нескольких чисел. Напишите программу, которая найдёт 
#сумму элементов списка, стоящих на нечётной позиции.
#Вариант А.
list = [1, 12, 5, 4 , 6, 2, 7, 3, 10, 18, 9]
print(list)
sum = 0
for i in range(len(list)):
    if i % 2 != 0:
        sum = sum + list[i]
print ("Сумма элементов на нечётных позициях равна: ",sum)
#Вариант В.
list = [i for i in range (1,11)]
print(list)
sum = 0
for i in range(len(list)):
    if i % 2 != 0:
        sum = sum + list[i]
print ("Сумма элементов на нечётных позициях равна: ",sum)

# Задача 3 
# Задайте список из вещественных чисел.Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Вариант А.
#def list(L):
#    list = []
#    for i in range(L):
#        n = float(input(f"Введите {i+1} элемент: "))
#        list.append(n)
#    return list
#m = int(input("Введите количество элементов: "))
#mylist = list(m)
#print(mylist)
#max = 0
#min = 1
#for i in mylist:
#    if (i - int(i)) <= min:
#        min = i - int(i)
#    if (i - int(i)) >= max:
#        max = i - int(i)  
#print(max - min)
#Вариант B.
mylist = list(map(float, input("Введите вещественные числа через пробел:\n").split()))
newlist = [round(i%1,2) for i in mylist if i%1 != 0]
print(max(newlist) - min(newlist))

# Задача 4 Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
#Вариант А.
ax = int(input("Введите координаты x точки A: "))
ay = int(input("Введите координаты y точки A: "))
bx = int(input("Введите координаты x точки B: "))
by = int(input("Введите координаты y точки B: "))

from math import sqrt
ab = sqrt((by-ay)**2+(bx-ax)**2), 2
print("Расстояние между точками А и В = ", ab )
#Вариант B.
def find_AB():
    AB = []
    text = input('введите координаты точки А - ')
    temp = text.split()
    A = list(map(int, temp))
    AB.append(A) 
    text = input('введите координаты точки B - ')
    temp = text.split()
    B = list(map(int, temp))
    AB.append(B)
    return AB
    
def find_distance_AB(AB):
    point1, point2 = AB
    AB_disane = 0
    for i in range(len(point1)):
        AB_temp = (point2[i]-point1[i])**2
        AB_disane += AB_temp
    return AB_disane**0.5
        
AB = find_AB()
print(AB)
print(find_distance_AB(AB))