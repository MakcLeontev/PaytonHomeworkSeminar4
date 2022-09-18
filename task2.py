# Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.
n=int(input('Введите число'))
k=n
arr=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
list_1=list()
if n in arr:
    print(n,'=',n)
else:
    while n>1:
        for i in range(len(arr)):
            if n%arr[i]==0:
                list_1.append(arr[i])
                n=n/arr[i]
                break
    print(*list_1, sep='*')        



