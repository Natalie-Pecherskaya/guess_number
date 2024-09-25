# Импорт функции получения случайных чисел
# из модуля random.
from random import randint

# Получаем случайное число в диапазоне от 1 до 100.
number = randint(1, 100)
print('Угадайте число от 1 до 100')

def main():
    counter = 0
    while True:
        # Получаем число от пользователя и сохраняем его в переменную.
        guess = int(input('Введите число: '))
        # Если число меньше загаданного...
        if guess < number:
            # ...выводим сообщение.
            counter += 1
            print('Ваше число меньше того, что загадано.')
            
        # Если число больше загаданного...
        if guess > number:
            # ...выводим сообщение.
            counter += 1
            print('Ваше число больше того, что загадано.')
        
        # Если число угадано...
        if guess == number:
            # ...прерываем выполнение программы и...
            counter += 1
            break
    # ...выводим сообщение.
    print('Отличная интуиция! Вы угадали число :)')
    print(f'Количество попыток - {counter}!')
    
main()