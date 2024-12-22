"""
GUNNER:
=================
Сложность: 7
-----------------
Игра "Артиллерист" - это игра, в которой игрок пытается поразить цель, находящуюся на определенном расстоянии, стреляя из пушки под заданным углом и с заданной начальной скоростью. В игре учитывается гравитация.
Цель игры состоит в том, чтобы подобрать правильный угол и скорость выстрела, чтобы снаряд достиг цели.
Правила игры:
1. Компьютер устанавливает случайное расстояние до цели.
2. Игрок вводит угол выстрела (в градусах) и начальную скорость снаряда.
3. Компьютер вычисляет траекторию снаряда, учитывая гравитацию.
4. Если снаряд попадает в цель (расстояние до цели в пределах погрешности), игрок выигрывает.
5. Если снаряд не попадает в цель, игрок может попробовать еще раз, пока не израсходует все попытки или не попадет в цель.
-----------------
Алгоритм:
1. Установить максимальное количество попыток (например, 10).
2. Сгенерировать случайное расстояние до цели в диапазоне от 100 до 1000.
3. Начать цикл "пока не кончились попытки":
    3.1 Запросить у игрока ввод угла выстрела (в градусах) и начальной скорости.
    3.2 Конвертировать угол из градусов в радианы.
    3.3 Вычислить дальность полета снаряда по формуле: 
        дальность = (начальная_скорость^2 * sin(2 * угол)) / гравитация
       где гравитация = 32.2
    3.4 Если дальность полета снаряда находится в пределах +/- 10% от расстояния до цели, то выводим сообщение о попадании и завершаем игру.
    3.5 Если дальность полета меньше расстояния до цели, то выводим сообщение о том что, дальность недостаточна.
    3.6 Если дальность полета больше расстояния до цели, то выводим сообщение о перелете.
4. Если все попытки исчерпаны, то выводим сообщение о проигрыше.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:
    <code><b>
    maxAttempts = 10
    gravity = 32.2
    targetDistance = random(100, 1000)
    attempt = 0
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: пока попытки не кончились"}
    LoopStart -- Да --> IncreaseAttempts["<code><b>attempt = attempt + 1</b></code>"]
    IncreaseAttempts --> InputAngleSpeed["<p align='left'>Ввод угла выстрела (в градусах)
    <code><b>angle</b></code> и начальной скорости
    <code><b>initialSpeed</b></code></p>"]
    InputAngleSpeed --> ConvertAngle["<code><b>angle = angle * pi / 180</b></code>"]
    ConvertAngle --> CalculateDistance["<p align='left'>Вычисление дальности полета
    <code><b>distance = (initialSpeed^2 * sin(2 * angle)) / gravity</b></code></p>"]
    CalculateDistance --> CheckHit{"<p align='left'>Проверка:
    <code><b>targetDistance - (targetDistance * 0.10)  &lt;= distance &lt;=  targetDistance + (targetDistance * 0.10) </b></code></p>"}
    CheckHit -- Да --> OutputWin["Вывод сообщения: <b>YOU HIT THE TARGET!</b>"]
    OutputWin --> End["Конец"]
    CheckHit -- Нет --> CheckShort{"Проверка: <code><b>distance &lt; targetDistance</b></code>?"}
    CheckShort -- Да --> OutputShort["Вывод сообщения: <b>TOO SHORT</b>"]
    OutputShort --> LoopStart
    CheckShort -- Нет --> OutputLong["Вывод сообщения: <b>TOO LONG</b>"]
    OutputLong --> LoopStart
    LoopStart -- Нет --> OutputLose["Вывод сообщения: <b>YOU LOSE!</b>"]
    OutputLose --> End
```
Legenda:
    Start - Начало программы.
    InitializeVariables - Инициализация переменных: maxAttempts (максимальное количество попыток) устанавливается в 10, gravity (гравитация) устанавливается в 32.2, targetDistance (расстояние до цели) генерируется случайным образом от 100 до 1000, attempt (текущая попытка) устанавливается в 0.
    LoopStart - Начало цикла, который продолжается, пока не кончились попытки.
    IncreaseAttempts - Увеличение счетчика попыток на 1.
    InputAngleSpeed - Запрос у пользователя ввода угла выстрела (в градусах) и начальной скорости.
    ConvertAngle - Конвертация угла из градусов в радианы.
    CalculateDistance - Вычисление дальности полета снаряда.
    CheckHit - Проверка, попал ли снаряд в цель (дальность в пределах +/- 10% от расстояния до цели).
    OutputWin - Вывод сообщения о победе, если снаряд попал в цель.
    End - Конец программы.
    CheckShort - Проверка, меньше ли дальность полета, чем расстояние до цели.
    OutputShort - Вывод сообщения "TOO SHORT", если дальность меньше цели.
    OutputLong - Вывод сообщения "TOO LONG", если дальность больше цели.
    OutputLose - Вывод сообщения "YOU LOSE!", если все попытки исчерпаны.
"""
import random
import math

# Инициализация параметров игры
maxAttempts = 10  # Максимальное количество попыток
gravity = 32.2  # Гравитация
targetDistance = random.randint(100, 1000)  # Случайное расстояние до цели
attempt = 0  # Счетчик попыток
accuracy = 0.1  # Погрешность в 10%

print(f"Расстояние до цели: {targetDistance}")

# Основной игровой цикл
while attempt < maxAttempts:
    attempt += 1
    print(f"Попытка {attempt} из {maxAttempts}")

    # Запрашиваем ввод данных у пользователя
    while True:
        try:
            angle = float(input("Введите угол выстрела (в градусах): "))
            initialSpeed = float(input("Введите начальную скорость: "))
            break
        except ValueError:
             print("Пожалуйста, введите числовое значение")


    # Преобразуем угол в радианы
    angle = math.radians(angle)

    # Вычисляем дальность полета
    distance = (initialSpeed ** 2 * math.sin(2 * angle)) / gravity

    # Проверяем, попал ли снаряд в цель
    if targetDistance * (1- accuracy) <= distance <= targetDistance * (1 + accuracy):
        print("ВЫ ПОПАЛИ В ЦЕЛЬ!")
        break
    elif distance < targetDistance:
        print("Слишком коротко!")
    else:
        print("Слишком далеко!")

# Выводим сообщение о поражении, если все попытки исчерпаны
if attempt == maxAttempts:
    print("Вы проиграли!")
"""
Объяснение кода:
1. **Импорт модулей:**
   - `import random`: Импортирует модуль `random` для генерации случайных чисел.
   - `import math`: Импортирует модуль `math` для математических операций, таких как `sin` и `radians`.

2. **Инициализация параметров игры:**
   - `maxAttempts = 10`: Устанавливает максимальное количество попыток в 10.
   - `gravity = 32.2`: Устанавливает значение гравитации.
   - `targetDistance = random.randint(100, 1000)`: Генерирует случайное расстояние до цели в диапазоне от 100 до 1000.
   - `attempt = 0`: Инициализирует счетчик попыток.
   - `accuracy = 0.1`: Устанавливает погрешность в 10% для попадания в цель.

3. **Основной игровой цикл `while attempt < maxAttempts:`:**
   - Цикл продолжается, пока количество попыток `attempt` меньше, чем максимальное количество попыток `maxAttempts`.
   - `attempt += 1`: Увеличивает счетчик попыток на 1.
   - `print(f"Попытка {attempt} из {maxAttempts}")`: Выводит номер текущей попытки.
   - **Ввод данных от пользователя:**
     - `while True:`: Бесконечный цикл для проверки корректности ввода.
     - `try...except ValueError`: Обрабатывает возможные ошибки ввода нечисловых значений.
     - `angle = float(input("Введите угол выстрела (в градусах): "))`: Запрашивает угол выстрела у пользователя.
     - `initialSpeed = float(input("Введите начальную скорость: "))`: Запрашивает начальную скорость выстрела у пользователя.
     - `break`: Выходит из цикла ввода, если данные введены корректно.
   - **Преобразование угла:**
     - `angle = math.radians(angle)`: Преобразует угол из градусов в радианы.
   - **Вычисление дальности полета:**
     - `distance = (initialSpeed ** 2 * math.sin(2 * angle)) / gravity`: Вычисляет дальность полета снаряда, используя формулу из физики.
   - **Проверка попадания:**
     - `if targetDistance * (1 - accuracy) <= distance <= targetDistance * (1 + accuracy):`: Проверяет, находится ли дальность полета в пределах +/- 10% от расстояния до цели.
     - `print("ВЫ ПОПАЛИ В ЦЕЛЬ!")`: Выводит сообщение о победе, если снаряд попал в цель.
     - `break`: Завершает цикл, если снаряд попал в цель.
     - `elif distance < targetDistance:`: Проверяет, если снаряд не долетел.
     - `print("Слишком коротко!")`: Выводит сообщение, что выстрел был слишком коротким.
     - `else:`: Если снаряд перелетел цель.
     - `print("Слишком далеко!")`: Выводит сообщение, что выстрел был слишком длинным.

4. **Проверка поражения:**
   - `if attempt == maxAttempts:`: Проверяет, если все попытки исчерпаны.
   - `print("Вы проиграли!")`: Выводит сообщение о поражении.
"""
