# Задание 4.
n = int(input('Введите целое положительное число: '))
M = -1
while n > 0:
    d = n % 10
    if d > M:
        M = d
    n = n // 10
print('Самая большая цифра в числе: ', M)
