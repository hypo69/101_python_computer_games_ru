"""
GUNNER:
=================
Сложность: 4
-----------------
Игра "GUNNER" - это симуляция стрельбы по мишени. Игрок вводит угол выстрела и его скорость, а компьютер рассчитывает, попадет ли снаряд в цель.
Игрок имеет 5 попыток и после каждой попытки, получает подсказку:
 - "TOO LOW" - если снаряд не долетел.
 - "TOO HIGH" - если снаряд перелетел.
 - "BINGO" - если снаряд попал в цель.

Правила игры:
1. Компьютер устанавливает случайное расстояние до цели от 100 до 1000 футов.
2. Игрок вводит угол выстрела в градусах (от 0 до 90) и скорость выстрела в футах в секунду.
3. Компьютер рассчитывает дальность полета снаряда по формуле: дальность = (скорость^2 * sin(2 * угол)) / 32.2
4. Компьютер сравнивает дальность полета с расстоянием до цели и сообщает результат: "TOO LOW", "TOO HIGH" или "BINGO".
5. Игрок имеет 5 попыток.
6. Игра заканчивается после 5 попыток или если игрок попал в цель.
-----------------
Алгоритм:
1. Установить количество попыток равным 5.
2. Сгенерировать случайное расстояние до цели в диапазоне от 100 до 1000.
3. Начать цикл, пока не закончатся попытки:
    3.1. Запросить у игрока угол выстрела и скорость выстрела.
    3.2. Рассчитать дальность полета снаряда по формуле: дальность = (скорость^2 * sin(2 * угол в радианах)) / 32.2.
    3.3. Если дальность полета равна расстоянию до цели, вывести "BINGO" и завершить игру.
    3.4. Если дальность полета меньше расстояния до цели, вывести "TOO LOW".
    3.5. Если дальность полета больше расстояния до цели, вывести "TOO HIGH".
    3.6. Уменьшить количество оставшихся попыток.
4. Если после 5 попыток цель не поражена, вывести сообщение о проигрыше.
5. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:
    <code><b>
    attemptsLeft = 5
    targetDistance = random(100, 1000)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: пока <code><b>attemptsLeft > 0</b></code>"}
    LoopStart -- Да --> InputAngleSpeed["Ввод угла (<code><b>angle</b></code>) и скорости (<code><b>speed</b></code>)"]
    InputAngleSpeed --> CalculateDistance["<p align='left'>Расчет дальности:
        <code><b>
        distance = (speed<sup>2</sup> * sin(2 * angle * pi / 180)) / 32.2
        </b></code></p>"]
    CalculateDistance --> CheckHit{"Проверка: <code><b>distance == targetDistance</b></code>?"}
    CheckHit -- Да --> OutputBingo["Вывод сообщения: <b>BINGO</b>"]
    OutputBingo --> End["Конец"]
    CheckHit -- Нет --> CheckLow{"Проверка: <code><b>distance < targetDistance</b></code>?"}
    CheckLow -- Да --> OutputLow["Вывод сообщения: <b>TOO LOW</b>"]
    OutputLow --> DecreaseAttempts["<code><b>attemptsLeft = attemptsLeft - 1</b></code>"]
    DecreaseAttempts --> LoopStart
    CheckLow -- Нет --> OutputHigh["Вывод сообщения: <b>TOO HIGH</b>"]
    OutputHigh --> DecreaseAttempts
    LoopStart -- Нет --> OutputLose["Вывод сообщения: <b>YOU LOSE</b>"]
    OutputLose --> End
```

Legenda:
    Start - Начало программы.
    InitializeVariables - Инициализация переменных: attemptsLeft (количество попыток) устанавливается в 5, а targetDistance (расстояние до цели) генерируется случайным образом от 100 до 1000.
    LoopStart - Начало цикла, который продолжается, пока количество оставшихся попыток (attemptsLeft) больше 0.
    InputAngleSpeed - Запрос у пользователя ввода угла выстрела (angle) и скорости (speed).
    CalculateDistance - Расчет дальности полета снаряда (distance) по формуле.
    CheckHit - Проверка, равно ли вычисленное расстояние (distance) заданному расстоянию до цели (targetDistance).
    OutputBingo - Вывод сообщения "BINGO", если дальность равна расстоянию до цели.
    End - Конец программы.
    CheckLow - Проверка, меньше ли дальность полета (distance) расстояния до цели (targetDistance).
    OutputLow - Вывод сообщения "TOO LOW", если дальность меньше цели.
    OutputHigh - Вывод сообщения "TOO HIGH", если дальность больше цели.
    DecreaseAttempts - Уменьшение количества оставшихся попыток на 1.
    OutputLose - Вывод сообщения "YOU LOSE", если после 5 попыток цель не поражена.
"""
import random
import math

# Инициализация количества попыток
attemptsLeft = 5
# Генерация случайного расстояния до цели от 100 до 1000 футов
targetDistance = random.randint(100, 1000)

# Основной игровой цикл
while attemptsLeft > 0:
    # Запрашиваем ввод угла и скорости выстрела
    try:
        angle = float(input("Введите угол выстрела в градусах (0-90): "))
        speed = float(input("Введите скорость выстрела в футах в секунду: "))
    except ValueError:
        print("Пожалуйста, введите числовые значения.")
        continue

    # Проверка ввода угла
    if not (0 <= angle <= 90):
        print("Угол должен быть в диапазоне от 0 до 90 градусов.")
        continue

    # Расчет дальности полета снаряда
    # Перевод угла в радианы
    angle_radians = math.radians(angle)
    distance = (speed**2 * math.sin(2 * angle_radians)) / 32.2

    # Проверка попадания
    if abs(distance - targetDistance) < 0.01: # Используем небольшую погрешность для сравнения
        print("BINGO!")
        break  # Завершаем игру при попадании в цель
    elif distance < targetDistance:
        print("TOO LOW") # Сообщаем, что снаряд не долетел
    else:
        print("TOO HIGH") # Сообщаем, что снаряд перелетел

    # Уменьшаем количество оставшихся попыток
    attemptsLeft -= 1

# Вывод сообщения о проигрыше, если попытки закончились
if attemptsLeft == 0:
    print("YOU LOSE")

"""
Объяснение кода:
1. **Импорт модулей**:
   - `import random`: Импортирует модуль `random`, который используется для генерации случайного расстояния до цели.
   - `import math`: Импортирует модуль `math`, который используется для математических вычислений (синус и перевод градусов в радианы).

2. **Инициализация переменных**:
   - `attemptsLeft = 5`: Инициализирует переменную `attemptsLeft` для отслеживания количества оставшихся попыток, начиная с 5.
   - `targetDistance = random.randint(100, 1000)`: Генерирует случайное целое число от 100 до 1000, представляющее расстояние до цели, и сохраняет его в `targetDistance`.

3. **Основной игровой цикл `while attemptsLeft > 0:`**:
   - Цикл выполняется, пока у игрока есть оставшиеся попытки.

4. **Ввод данных**:
   - `try...except ValueError`: Блок try-except обрабатывает возможные ошибки ввода. Если пользователь введет не числовое значение, то будет выведено сообщение об ошибке.
   - `angle = float(input("Введите угол выстрела в градусах (0-90): "))`: Запрашивает у пользователя угол выстрела и преобразует его в число с плавающей точкой.
   - `speed = float(input("Введите скорость выстрела в футах в секунду: "))`: Запрашивает у пользователя скорость выстрела и преобразует ее в число с плавающей точкой.

5. **Проверка ввода угла**:
   - `if not (0 <= angle <= 90):`: Проверяет, находится ли введенный угол в допустимом диапазоне (от 0 до 90 градусов).
   - `print("Угол должен быть в диапазоне от 0 до 90 градусов.")`: Выводит сообщение об ошибке, если угол введен неверно.
   - `continue`: Переходит к следующей итерации цикла, не выполняя остальной код в текущей итерации.

6. **Расчет дальности полета**:
   - `angle_radians = math.radians(angle)`: Преобразует угол из градусов в радианы, так как функция `math.sin()` ожидает радианы.
   - `distance = (speed**2 * math.sin(2 * angle_radians)) / 32.2`: Вычисляет дальность полета снаряда по заданной формуле.

7. **Проверка попадания**:
    -   `if abs(distance - targetDistance) < 0.01:`: Проверяет, попал ли снаряд в цель. Используется `abs()` для получения абсолютного значения разницы и небольшая погрешность (0.01) для сравнения чисел с плавающей точкой из-за неточностей представления.
    -   `print("BINGO!")`: Выводит сообщение о попадании.
    -   `break`: Завершает цикл (игру) при попадании.
    -   `elif distance < targetDistance:`: Проверяет, если снаряд не долетел.
    -   `print("TOO LOW")`: Выводит сообщение, что снаряд не долетел.
    -   `else:`: Если снаряд перелетел.
    -   `print("TOO HIGH")`: Выводит сообщение, что снаряд перелетел.
8. **Уменьшение количества попыток**:
    - `attemptsLeft -= 1`: Уменьшает количество оставшихся попыток на 1.

9. **Вывод сообщения о проигрыше**:
    -   `if attemptsLeft == 0:`: Проверяет, закончились ли попытки.
    -   `print("YOU LOSE")`: Выводит сообщение о проигрыше.
"""
