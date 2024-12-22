"""
STARS:
=================
Сложность: 4
-----------------
Игра "Звезды" представляет собой простую текстовую игру, в которой игрок управляет положением "звезды" на экране, вводя команды для ее перемещения. Цель игры - переместить звезду в правый нижний угол экрана.

Правила игры:
1. Изначально звезда находится в левом верхнем углу экрана (позиция 1,1).
2. Игрок вводит команды перемещения:
   - 'R' - переместить звезду вправо
   - 'L' - переместить звезду влево
   - 'U' - переместить звезду вверх
   - 'D' - переместить звезду вниз
3. Экран представляет собой сетку 12x12.
4. Игра заканчивается, когда звезда достигает правого нижнего угла экрана (позиция 12,12).
-----------------
Алгоритм:
1. Установить начальную позицию звезды в (1, 1).
2. Вывести на экран начальное расположение звезды, изображая ее символом "*".
3. Начать цикл:
    3.1 Запросить ввод команды перемещения ('R', 'L', 'U', 'D').
    3.2 Обновить позицию звезды в зависимости от введенной команды.
    3.3 Проверить, достигла ли звезда позиции (12, 12). Если да, вывести сообщение о победе и завершить игру.
    3.4 Иначе вывести на экран новое расположение звезды.
4. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializePosition["<p align='left'>Инициализация позиции звезды:
    <code><b>
    starRow = 1
    starCol = 1
    </b></code></p>"]
    InitializePosition --> DisplayBoard["Вывод начального положения звезды"]
    DisplayBoard --> LoopStart{"Начало цикла"}
    LoopStart --> InputMove["Ввод команды перемещения (R, L, U, D)"]
    InputMove --> UpdatePosition["<p align='left'>Обновление позиции звезды:
    <code><b>
    starRow, starCol = updatePosition(command, starRow, starCol)
    </b></code></p>"]
    UpdatePosition --> CheckWin{"Проверка: <code><b>starRow == 12 and starCol == 12?</b></code>"}
    CheckWin -- Да --> OutputWin["Вывод сообщения: <b>YOU MADE IT!</b>"]
    OutputWin --> End["Конец"]
    CheckWin -- Нет --> DisplayBoardUpdated["Вывод нового положения звезды"]
    DisplayBoardUpdated --> LoopStart
```

Legenda:
    Start - Начало программы.
    InitializePosition - Инициализация начальной позиции звезды: starRow (строка) и starCol (столбец) устанавливаются в 1.
    DisplayBoard - Вывод на экран начального расположения звезды.
    LoopStart - Начало игрового цикла.
    InputMove - Запрос у игрока команды для перемещения звезды ('R', 'L', 'U', 'D').
    UpdatePosition - Обновление позиции звезды на основе введенной команды.
    CheckWin - Проверка, достигла ли звезда конечной позиции (12, 12).
    OutputWin - Вывод сообщения о победе, если звезда достигла конечной позиции.
    End - Конец программы.
    DisplayBoardUpdated - Вывод на экран обновленного положения звезды.
"""
__author__ = 'hypo69 (hypo69@davidka.net)'

# Инициализация начальной позиции звезды
starRow = 1
starCol = 1
# Размер игровой доски
boardSize = 12

def printBoard(starRow, starCol):
  """
  Выводит на экран игровое поле с текущей позицией звезды.
  Аргументы:
    starRow (int): строка, в которой находится звезда.
    starCol (int): столбец, в котором находится звезда.
  """
  for row in range(1, boardSize + 1):
    line = ""
    for col in range(1, boardSize + 1):
      if row == starRow and col == starCol:
        line += "*"  # Отображаем звезду
      else:
        line += "."  # Отображаем пустую клетку
    print(line)

def updatePosition(command, starRow, starCol):
    """
    Обновляет позицию звезды на основе введенной команды.
    Аргументы:
        command (str): команда перемещения ('R', 'L', 'U', 'D').
        starRow (int): текущая строка звезды.
        starCol (int): текущий столбец звезды.
    Возвращает:
        tuple (int, int): новая строка и столбец звезды.
    """
    if command == 'R':  # Двигаемся вправо
        if starCol < boardSize:
           starCol += 1
    elif command == 'L':  # Двигаемся влево
        if starCol > 1:
            starCol -= 1
    elif command == 'U':  # Двигаемся вверх
        if starRow > 1:
            starRow -= 1
    elif command == 'D':  # Двигаемся вниз
        if starRow < boardSize:
            starRow += 1
    return starRow, starCol

# Вывод начального положения звезды
printBoard(starRow, starCol)

# Основной игровой цикл
while True:
    # Запрос команды перемещения у пользователя
    command = input("Введите команду (R/L/U/D): ").upper()

    # Обновление позиции звезды на основе введенной команды
    starRow, starCol = updatePosition(command, starRow, starCol)

    # Вывод нового положения звезды на экран
    printBoard(starRow, starCol)

    # Проверка, достигла ли звезда конечной позиции
    if starRow == boardSize and starCol == boardSize:
        print("ПОЗДРАВЛЯЮ! Вы переместили звезду в правый нижний угол!")
        break  # Завершаем игру

"""
Объяснение кода:
1.  **Инициализация переменных**:
    -   `starRow = 1`:  Начальная строка звезды (верхняя строка).
    -   `starCol = 1`:  Начальный столбец звезды (левый столбец).
    -   `boardSize = 12`: Размер игрового поля (12x12).
2.  **Функция `printBoard(starRow, starCol)`**:
    -  Принимает текущие координаты звезды (строку `starRow` и столбец `starCol`).
    -   Выводит игровое поле в консоль. Звезда '*' обозначает текущую позицию звезды, а '.' - пустые клетки.
    -   Использует два вложенных цикла для прохода по всем строкам и столбцам поля.
3.  **Функция `updatePosition(command, starRow, starCol)`**:
    -   Принимает команду перемещения (`command`) и текущие координаты звезды (`starRow`, `starCol`).
    -   Обновляет координаты звезды в зависимости от команды ('R', 'L', 'U', 'D'):
        -   'R': Двигается вправо, если не достигнут правый край.
        -   'L': Двигается влево, если не достигнут левый край.
        -   'U': Двигается вверх, если не достигнут верхний край.
        -   'D': Двигается вниз, если не достигнут нижний край.
    -   Возвращает новую позицию звезды (строку и столбец).
4.  **Вывод начального положения звезды**:
    -   `printBoard(starRow, starCol)`: Выводит на экран игровое поле с начальным положением звезды.
5.  **Основной игровой цикл `while True`**:
    -   Бесконечный цикл, пока не выполнится условие победы.
    -   `command = input("Введите команду (R/L/U/D): ").upper()`: Запрашивает у пользователя команду перемещения и преобразует ее в верхний регистр.
    -   `starRow, starCol = updatePosition(command, starRow, starCol)`: Обновляет позицию звезды, вызывая функцию `updatePosition()`.
    -   `printBoard(starRow, starCol)`: Выводит обновленное положение звезды на экран.
    -   `if starRow == boardSize and starCol == boardSize`: Проверяет, достигла ли звезда правого нижнего угла (12,12).
    -   `print("ПОЗДРАВЛЯЮ! Вы переместили звезду в правый нижний угол!")`: Выводит сообщение о победе.
    -   `break`: Завершает игровой цикл (игру).
"""
