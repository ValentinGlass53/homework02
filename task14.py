"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k
), не превосходящие числа N.
10 -> 1 2 4 8
"""
num = int(input('ВВедите число'))
count = 1
i = 1
while count < num:
   if count*2 < num:
      count*=2
      i+=1
      print(count)
   else:
       break
