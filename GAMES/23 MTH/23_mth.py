
<23 MTH>:
=================
Сложность: 3
-----------------
Игра "Угадай число" - это классическая игра, в которой компьютер выбирает случайное число в диапазоне от 1 до 100, а игрок должен угадать это число, получая подсказки "слишком низко" или "слишком высоко" после каждой попытки. 
Игра продолжается до тех пор, пока игрок не угадает число.

Правила игры:
1. Компьютер выбирает случайное целое число от 1 до 100.
2. Игрок вводит свои предположения о загаданном числе.
3. После каждой попытки компьютер сообщает, было ли введенное число слишком низким, слишком высоким или угадано.
4. Игра продолжается до тех пор, пока игрок не угадает загаданное число.
-----------------
Алгоритм:
1.  Установить число попыток в 0.
2.  Сгенерировать случайное число в диапазоне от 1 до 100.
3.  Начать цикл "пока число не угадано":
    3.1 Увеличить число попыток на 1.
    3.2 Запросить у игрока ввод числа.
    3.3 Если введенное число равно загаданному числу, перейти к шагу 4.
    3.4 Если введенное число меньше загаданного числа, вывести сообщение "TOO LOW".
    3.5 Если введенное число больше загаданного числа, вывести сообщение "TOO HIGH".
4. Вывести сообщение "YOU GOT IT IN {число попыток} GUESSES!"
5. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:
    <code><b>
    numberOfGuesses = 0
    targetNumber = random(1, 100)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: пока не угадано"}
    LoopStart -- Да --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["Ввод числа пользователем: <code><b>userGuess</b></code>"]
    InputGuess --> CheckGuess{"Проверка: <code><b>userGuess == targetNumber?</b></code>"}
    CheckGuess -- Да --> OutputWin["Вывод сообщения: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["Конец"]
    CheckGuess -- Нет --> CheckLow{"Проверка: <code><b>userGuess &lt; targetNumber</b></code>?"}
    CheckLow -- Да --> OutputLow["Вывод сообщения: <b>TOO LOW</b>"]
    OutputLow --> LoopStart
    CheckLow -- Нет --> OutputHigh["Вывод сообщения: <b>TOO HIGH</b>"]
    OutputHigh --> LoopStart
    LoopStart -- Нет --> End
```
**Legenda:**
    Start - Начало программы.
    InitializeVariables - Инициализация переменных: numberOfGuesses (количество попыток) устанавливается в 0, а targetNumber (загаданное число) генерируется случайным образом от 1 до 100.
    LoopStart - Начало цикла, который продолжается, пока число не угадано.
    IncreaseGuesses - Увеличение счетчика количества попыток на 1.
    InputGuess - Запрос у пользователя ввода числа и сохранение его в переменной userGuess.
    CheckGuess - Проверка, равно ли введенное число userGuess загаданному числу targetNumber.
    OutputWin - Вывод сообщения о победе, если числа равны, с указанием количества попыток.
    End - Конец программы.
    CheckLow - Проверка, меньше ли введенное число userGuess загаданного числа targetNumber.
    OutputLow - Вывод сообщения "TOO LOW", если введенное число меньше загаданного.
    OutputHigh - Вывод сообщения "TOO HIGH", если введенное число больше загаданного.
"""
import random

# Инициализация счетчика попыток
numberOfGuesses = 0
# Генерируем случайное число от 1 до 100
targetNumber = random.randint(1, 100)

# Основной игровой цикл
while True:
    # Увеличиваем количество попыток
    numberOfGuesses += 1
    # Запрашиваем ввод числа у пользователя
    try:
        userGuess = int(input("Угадай число от 1 до 100: "))
    except ValueError:
        print("Пожалуйста, введите целое число.")
        continue

    # Проверяем, угадано ли число
    if userGuess == targetNumber:
        print(f"ПОЗДРАВЛЯЮ! Вы угадали число за {numberOfGuesses} попыток!")
        break  # Завершаем цикл, если число угадано
    elif userGuess < targetNumber:
        print("Слишком низко")  # Сообщаем, что загаданное число больше
    else:
        print("Слишком высоко")  # Сообщаем, что загаданное число меньше
```
Объяснение кода:
1. **Импорт модуля `random`**:
   - `import random`: Импортирует модуль `random`, который используется для генерации случайного числа.
2. **Инициализация переменных**:
    -  `numberOfGuesses = 0`:  Инициализирует переменную `numberOfGuesses` для подсчета количества попыток игрока.
    -  `targetNumber = random.randint(1, 100)`: Генерирует случайное целое число в диапазоне от 1 до 100 и сохраняет его в переменной `targetNumber`. Это число, которое игрок должен угадать.
3. **Основной игровой цикл `while True:`**:
    -  `while True:`: Начинает бесконечный цикл, который будет продолжаться до тех пор, пока игрок не угадает число.
    -  `numberOfGuesses += 1`: Увеличивает счетчик попыток на 1.
    -  **Обработка ввода пользователя**:
        -  `try...except ValueError:`: Используется для обработки возможных ошибок при вводе данных пользователем.
        - `userGuess = int(input("Угадай число от 1 до 100: "))`: Выводит сообщение с запросом ввода числа от 1 до 100 и сохраняет результат в `userGuess`. `int()` преобразует строку, введенную пользователем, в целое число.
        - `except ValueError:`: Если пользователь введет что-то, что нельзя преобразовать в целое число,  выводится сообщение об ошибке и программа переходит к следующей итерации цикла.
    -   **Проверка условия победы**:
        -   `if userGuess == targetNumber:`: Проверяет, равно ли введенное пользователем число (`userGuess`) загаданному числу (`targetNumber`).
        -   `print(f"ПОЗДРАВЛЯЮ! Вы угадали число за {numberOfGuesses} попыток!")`: Если числа равны, выводит поздравительное сообщение с указанием количества попыток.
        -   `break`: Завершает цикл `while`, и игра заканчивается.
    -   **Подсказки пользователю**:
        - `elif userGuess < targetNumber:`: Если введенное число меньше загаданного, то выводит сообщение "Слишком низко".
        - `else:`: Если введенное число не равно и не меньше загаданного, то оно больше, и выводится сообщение "Слишком высоко".
```