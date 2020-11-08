#рулетка
import random
random_number = random.randint(1,10)
i = 1
print("Машина выбрала случайное число от 1 до 10. У вас 3 попытки, чтобы угадать")
while i <= 3:
    u = int(input(str(i) + '-я попытка: '))
    if u != random_number:
        print('попробуйте еще раз, у вас осталось - ' + str(3-i) + ' вариант(ов)')
    else:
        print('Вы угадали, - это ' + str(u) + 'You won!')
        break
    i += 1
else:
    print('You lose! Попытки закончились, машина выбрала число - ', + random_number)