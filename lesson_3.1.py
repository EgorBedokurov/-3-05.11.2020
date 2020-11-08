#вариант №1 - "некрасиво", просто эксперементировал
s_n=int(input('введите трехзначное число - '))
a=s_n//100
b=(s_n//10)%10
c=s_n%10
print(a+b+c)

#вариант №2 - рабочий, можно посчитать сумму цифр любого числа
some_numb=int(input('insert number - '))
rand=str(some_numb)
s_m=0
for i in range(len(rand)):
    s_m+=int(rand[i])
print(s_m)

