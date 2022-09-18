# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

list_1 = [int(i) for i in input().split()]
list_2=list()
for i in range(len(list_1)):
    if list_1.count(list_1[i])==1:
        list_2.append(list_1[i])
print(*list_2)
        

    

      
    




