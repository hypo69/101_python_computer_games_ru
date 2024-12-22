"""
<BOWL>:
=================
Сложность: 5
-----------------
Игра "Боулинг" - это текстовая симуляция игры в боулинг, где игрок бросает мяч, а компьютер определяет количество сбитых кеглей.
Игра состоит из 10 раундов. В каждом раунде игрок имеет два броска, если только не выбивает страйк (сбивает все кегли) первым броском. Результат каждого раунда накапливается, формируя общий счёт.

Правила игры:
1. В начале каждого раунда игрок имеет 10 кеглей.
2. Игрок бросает мяч (вводится случайное число от 0 до 10).
3. Количество сбитых кеглей вычитается из общего количества кеглей.
4. Если игрок сбил все 10 кеглей первым броском (страйк), раунд заканчивается, и ход переходит к следующему раунду.
5. Если игрок не выбил страйк, он делает второй бросок.
6. Результаты каждого раунда суммируются для общего счета.
7. Игра состоит из 10 раундов.
8. По окончании игры выводится общий счет игрока.
-----------------
Алгоритм:
1.  Установить общий счет (totalScore) в 0.
2.  Начать цикл от 1 до 10 (для 10 раундов):
    2.1 Установить количество кеглей (pins) в 10.
    2.2 Вывести номер текущего раунда.
    2.3 Сгенерировать случайное число от 0 до количества оставшихся кеглей (pins) (первый бросок).
    2.4 Вывести сообщение о количестве сбитых кеглей (firstThrow).
    2.5 Вычесть количество сбитых кеглей (firstThrow) из общего количества кеглей (pins).
    2.6 Если количество сбитых кеглей равно 10 (страйк), перейти к шагу 2.10.
    2.7 Сгенерировать случайное число от 0 до количества оставшихся кеглей (pins) (второй бросок).
    2.8 Вывести сообщение о количестве сбитых кеглей (secondThrow).
    2.9 Вычесть количество сбитых кеглей (secondThrow) из общего количества кеглей (pins).
    2.10 Добавить сумму сбитых кеглей (firstThrow + secondThrow) к общему счету (totalScore).
3.  Вывести общий счет (totalScore).
4. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeScore["Инициализация: totalScore = 0"]
    InitializeScore --> RoundLoopStart{"Начало цикла: для 10 раундов"}
    RoundLoopStart -- Да --> ResetPins["pins = 10"]
    ResetPins --> DisplayRound["Вывод: 'Раунд' + roundNumber"]
    DisplayRound --> FirstThrow["firstThrow = random(0, pins)"]
    FirstThrow --> OutputFirstThrow["Вывод: 'Первый бросок:' + firstThrow"]
    OutputFirstThrow --> UpdatePins1["pins = pins - firstThrow"]
    UpdatePins1 --> CheckStrike{"Проверка: firstThrow == 10?"}
    CheckStrike -- Да --> UpdateTotalScoreStrike["totalScore = totalScore + firstThrow"]
    UpdateTotalScoreStrike --> RoundLoopEnd["Конец раунда"]
    CheckStrike -- Нет --> SecondThrow["secondThrow = random(0, pins)"]
    SecondThrow --> OutputSecondThrow["Вывод: 'Второй бросок:' + secondThrow"]
    OutputSecondThrow --> UpdatePins2["pins = pins - secondThrow"]
    UpdatePins2 --> UpdateTotalScore["totalScore = totalScore + firstThrow + secondThrow"]
    UpdateTotalScore --> RoundLoopEnd
    RoundLoopStart -- Нет --> OutputTotalScore["Вывод: 'Общий счет:' + totalScore"]
    OutputTotalScore --> End["Конец"]
    RoundLoopEnd --> RoundLoopStart
```
    
**Legenda:**
    Start - Начало программы.
    InitializeScore - Инициализация переменной totalScore (общий счет) значением 0.
    RoundLoopStart - Начало цикла, который выполняется 10 раз (для каждого раунда).
    ResetPins - Установка количества кеглей pins в 10.
    DisplayRound - Вывод номера текущего раунда.
    FirstThrow - Генерация случайного числа от 0 до текущего количества кеглей, представляющего первый бросок.
    OutputFirstThrow - Вывод количества сбитых кеглей первым броском.
    UpdatePins1 - Обновление количества оставшихся кеглей после первого броска.
    CheckStrike - Проверка, был ли первый бросок страйком (сбиты все 10 кеглей).
    UpdateTotalScoreStrike - Обновление общего счета totalScore, если был страйк.
    RoundLoopEnd - Конец текущего раунда.
    SecondThrow - Генерация случайного числа от 0 до текущего количества кеглей, представляющего второй бросок.
    OutputSecondThrow - Вывод количества сбитых кеглей вторым броском.
    UpdatePins2 - Обновление количества оставшихся кеглей после второго броска.
    UpdateTotalScore - Обновление общего счета totalScore суммой сбитых кеглей за оба броска.
    OutputTotalScore - Вывод общего счета после завершения всех раундов.
    End - Конец программы.
"""
import random

# Инициализация общего счета
totalScore = 0

# Цикл для 10 раундов игры
for roundNumber in range(1, 11):
    # В начале каждого раунда у нас 10 кеглей
    pins = 10
    print(f"Раунд {roundNumber}")

    # Первый бросок
    firstThrow = random.randint(0, pins)
    print(f"Первый бросок: {firstThrow}")
    pins -= firstThrow

    # Проверка на страйк
    if firstThrow == 10:
        totalScore += firstThrow
        print("Страйк!")
        continue # Переход к следующему раунду
    
    # Второй бросок (если не было страйка)
    secondThrow = random.randint(0, pins)
    print(f"Второй бросок: {secondThrow}")
    pins -= secondThrow

    # Обновление общего счета
    totalScore += firstThrow + secondThrow

# Вывод общего счета
print(f"Общий счет: {totalScore}")

"""
Объяснение кода:
1.  **Импорт модуля `random`**:
   -  `import random`: Импортирует модуль `random`, который используется для генерации случайных чисел для имитации бросков.
2.  **Инициализация общего счета**:
   -  `totalScore = 0`: Инициализирует переменную `totalScore` для хранения общего количества очков, начальное значение 0.
3.  **Цикл по раундам**:
   -  `for roundNumber in range(1, 11):`:  Цикл, проходящий 10 раз (для каждого раунда игры).
   - `pins = 10`: В начале каждого раунда количество кеглей устанавливается в 10.
   -  `print(f"Раунд {roundNumber}")`: Выводит номер текущего раунда.
4. **Первый бросок**:
    -  `firstThrow = random.randint(0, pins)`: Генерируется случайное число от 0 до количества оставшихся кеглей (pins) для имитации первого броска.
    - `print(f"Первый бросок: {firstThrow}")`: Выводит количество сбитых кеглей первым броском.
    - `pins -= firstThrow`:  Количество сбитых кеглей вычитается из общего количества кеглей.
5.  **Проверка на страйк**:
    -  `if firstThrow == 10:`: Проверяет, был ли первый бросок страйком (сбиты все 10 кеглей).
    -  `totalScore += firstThrow`: Если был страйк, добавляет 10 очков к общему счету.
    -  `print("Страйк!")`:  Выводит сообщение о страйке.
    - `continue`:  Переходит к следующей итерации цикла (следующему раунду), не выполняя оставшийся код в текущем раунде.
6.  **Второй бросок (если не было страйка)**:
    -  `secondThrow = random.randint(0, pins)`: Генерируется случайное число от 0 до количества оставшихся кеглей для имитации второго броска.
    - `print(f"Второй бросок: {secondThrow}")`: Выводит количество сбитых кеглей вторым броском.
    -  `pins -= secondThrow`: Количество сбитых кеглей вычитается из общего количества кеглей.
7.  **Обновление общего счета**:
    -  `totalScore += firstThrow + secondThrow`: К общему счету добавляется сумма очков за первый и второй броски.
8.  **Вывод общего счета**:
    -  `print(f"Общий счет: {totalScore}")`: Выводит финальный общий счет после всех 10 раундов.
"""
