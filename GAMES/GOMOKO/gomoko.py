
<GOMOKO>:
=================
Сложность: 5
-----------------
Игра "Гомоку" (также известная как "Пять в ряд") - это стратегическая настольная игра для двух игроков. Игроки по очереди ставят свои фишки (обычно крестики и нолики) на игровое поле, стремясь выстроить непрерывную линию из пяти своих фишек по вертикали, горизонтали или диагонали. Игра заканчивается, когда один из игроков достигает этого условия, или когда все поле заполнено, и в этом случае объявляется ничья.
В этой версии игры поле представлено матрицей 15x15, а ходы игрока и компьютера делаются поочередно. Компьютер использует простой алгоритм для выбора своего хода. Игроки вводят свои ходы в виде координат x и y.
Правила игры:
1. Игра проходит на доске 15x15.
2. Игроки ходят по очереди, ставя свои фишки (крестик 'X' для первого игрока, нолик 'O' для второго).
3. Цель игры - первым выстроить непрерывную линию из пяти своих фишек по вертикали, горизонтали или диагонали.
4. Игра заканчивается победой одного из игроков или ничьей, если доска полностью заполнена и никто не построил линию из пяти.
5. Игроки вводят свои ходы в виде координат x и y.
-----------------
Алгоритм:
1.  Инициализация:
    1.1.  Создать пустую доску 15x15 (массив A).
    1.2.  Установить признак начала игры `G = 1`.
    1.3.  Установить флаг текущего игрока в 1 (`P=1`).
2.  Начать цикл игры, пока G равно 1
    2.1.  Вывести текущее состояние доски на экран.
    2.2. Если текущий игрок 1:
        2.2.1 Запросить у пользователя координаты хода X, Y.
        2.2.2 Проверить допустимость хода: если ячейка A[X,Y] не пуста, запросить ввод хода повторно.
        2.2.3 Поставить на доску A[X,Y] символ хода текущего игрока (в случае P=1 это "X").
        2.2.4 Изменить флаг игрока P=2.
     2.3 Если текущий игрок 2:
        2.3.1 Компьютер выбирает случайный ход, пока не найдет пустую ячейку.
        2.3.2 Поставить на доску A[X,Y] символ хода текущего игрока (в случае P=2 это "O").
        2.3.3 Изменить флаг игрока P=1.
     2.4 Проверить, есть ли победитель или доска заполнена:
        2.4.1 Если есть линия из пяти, то вывести сообщение о победителе и присвоить `G = 0` (закончить игру).
        2.4.2 Если доска заполнена и победителя нет, вывести сообщение о ничьей и присвоить `G = 0` (закончить игру).
3. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeBoard["Инициализация: <br>Создание доски 15x15; <br>G = 1 (флаг игры); <br>P = 1 (игрок 1)"]
    InitializeBoard --> GameLoopStart{"Начало цикла игры:<br>while G == 1"}
    GameLoopStart --> DisplayBoard["Вывод текущего состояния доски"]
    DisplayBoard --> CheckPlayer{"Проверка: <br>P == 1 (ход игрока)?"]
    CheckPlayer -- Да --> PlayerInput["Ввод хода игрока (X, Y)"]
     PlayerInput --> ValidatePlayerMove{"Проверка допустимости хода:<br>Ячейка A[X,Y] пуста?"}
     ValidatePlayerMove -- Нет --> PlayerInput
      ValidatePlayerMove -- Да --> UpdateBoardPlayer["Обновление доски:<br>A[X, Y] = 'X'"]
    UpdateBoardPlayer --> ChangePlayerP1["Переключение игрока: P = 2"]
     ChangePlayerP1 --> CheckWinOrFull["Проверка победы или заполненности доски"]
      CheckPlayer -- Нет --> ComputerMove["Ход компьютера: выбор пустой ячейки (X, Y)"]
    ComputerMove --> UpdateBoardComputer["Обновление доски:<br>A[X, Y] = 'O'"]
    UpdateBoardComputer --> ChangePlayerP2["Переключение игрока: P = 1"]
     ChangePlayerP2 --> CheckWinOrFull
    CheckWinOrFull -- Победитель --> OutputWinner["Вывод сообщения о победе; <br> G = 0"]
    OutputWinner --> End["Конец"]
    CheckWinOrFull -- Доска заполнена --> OutputDraw["Вывод сообщения о ничьей; <br> G = 0"]
    OutputDraw --> End
     CheckWinOrFull -- Нет --> GameLoopStart
    GameLoopStart -- Нет --> End

```
Legenda:
    Start - Начало игры.
    InitializeBoard - Инициализация игрового поля (доски) размером 15x15, установка флага игры G в 1 и установка текущего игрока P в 1.
    GameLoopStart - Начало основного цикла игры, который продолжается пока флаг игры G равен 1.
    DisplayBoard - Вывод на экран текущего состояния игрового поля.
    CheckPlayer - Проверка, чей сейчас ход: если P равно 1, то ход игрока, иначе ход компьютера.
    PlayerInput - Ввод игроком координат X и Y для своего хода.
    ValidatePlayerMove - Проверка, является ли выбранная игроком ячейка пустой (допустимый ход). Если ячейка не пустая, запрашивает ввод хода повторно.
    UpdateBoardPlayer - Обновление доски: установка символа 'X' в выбранную игроком ячейку.
    ChangePlayerP1 - Переключение на второго игрока: P становится равным 2 (ход компьютера).
     ComputerMove - Ход компьютера: выбор пустой ячейки.
    UpdateBoardComputer - Обновление доски: установка символа 'O' в выбранную компьютером ячейку.
    ChangePlayerP2 - Переключение на первого игрока: P становится равным 1 (ход игрока).
    CheckWinOrFull - Проверка, есть ли победитель или заполнено ли игровое поле.
    OutputWinner - Вывод сообщения о победе и установка флага игры G в 0 для завершения цикла.
    OutputDraw - Вывод сообщения о ничьей и установка флага игры G в 0 для завершения цикла.
    End - Конец игры.
"""
__author__ = 'hypo69 (hypo69@davidka.net)'

import random

# 1. Инициализация:
# 1.1. Создаем пустую доску 15x15
board = [[' ' for _ in range(15)] for _ in range(15)]
# 1.2. Устанавливаем флаг начала игры G = 1
game_on = True
# 1.3. Устанавливаем флаг игрока, P = 1 (игрок 1 ходит первым)
current_player = 1

# Функция для вывода доски в консоль
def print_board(board):
    print("   ", end="")
    for i in range(15):
         print(f"{i:2}", end=" ")
    print()
    print("  " + "----" * 15)
    for i, row in enumerate(board):
        print(f"{i:2}|", end=" ")
        for cell in row:
            print(f"{cell:2}", end=" ")
        print()
    print()


# Функция проверки наличия победной линии
def check_winner(board, player):
    symbol = 'X' if player == 1 else 'O'
    # Проверка горизонтальных линий
    for row in board:
        for i in range(len(row) - 4):
            if row[i] == row[i + 1] == row[i + 2] == row[i + 3] == row[i + 4] == symbol:
                return True
    # Проверка вертикальных линий
    for col in range(15):
        for i in range(15 - 4):
            if board[i][col] == board[i + 1][col] == board[i + 2][col] == board[i + 3][col] == board[i + 4][col] == symbol:
                 return True
    # Проверка диагоналей (сверху-слева направо-вниз)
    for row in range(15 - 4):
        for col in range(15 - 4):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == board[row+4][col+4] == symbol:
                 return True
    # Проверка диагоналей (сверху-справа налево-вниз)
    for row in range(15 - 4):
        for col in range(4, 15):
            if board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3] == board[row+4][col-4] == symbol:
                 return True
    return False


# Функция проверки ничьей
def check_full_board(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False # Если есть хотя бы одна свободная ячейка, то игра не окончена
    return True  # Если нет пустых ячеек - ничья

# 2. Основной игровой цикл
while game_on:
    # 2.1. Выводим текущее состояние доски
    print_board(board)

    # 2.2. Ход игрока (P = 1)
    if current_player == 1:
        while True:
             try:
                # 2.2.1. Запрашиваем координаты хода X, Y
                x = int(input("Игрок 1 (X) введите x (0-14): "))
                y = int(input("Игрок 1 (X) введите y (0-14): "))

                # 2.2.2. Проверяем допустимость хода:
                if 0 <= x < 15 and 0 <= y < 15 and board[x][y] == ' ':
                    # 2.2.3. Ставим на доску символ хода текущего игрока (X)
                    board[x][y] = 'X'
                    break
                else:
                    print("Недопустимый ход. Попробуйте еще раз.")
             except ValueError:
                  print("Некорректный ввод. Пожалуйста, введите целые числа")
        # 2.2.4. Меняем флаг игрока
        current_player = 2
    # 2.3. Ход компьютера (P = 2)
    else:
        print("Ход компьютера:")
        while True:
            # 2.3.1. Компьютер выбирает случайный ход
            x = random.randint(0, 14)
            y = random.randint(0, 14)
            if board[x][y] == ' ':
                 # 2.3.2. Ставим на доску символ хода текущего игрока (O)
                board[x][y] = 'O'
                break

        # 2.3.3. Меняем флаг игрока
        current_player = 1

    # 2.4. Проверка на победителя или ничью
    if check_winner(board, 1 if current_player == 2 else 2 ):
        print_board(board)
        print(f"Победил игрок {'1 (X)' if current_player == 2 else '2 (O)'}!")
        game_on = False  # Завершаем игру
    elif check_full_board(board):
         print_board(board)
         print("Ничья!")
         game_on = False  # Завершаем игру

"""
Объяснение кода:
1.  **Инициализация**:
    -   `board = [[' ' for _ in range(15)] for _ in range(15)]`: Создает игровое поле 15x15, заполненное пробелами (пустые ячейки).
    -   `game_on = True`: Устанавливает флаг, сигнализирующий, что игра продолжается.
    -   `current_player = 1`: Устанавливает текущего игрока на первого (игрок 1).

2.  **Функция `print_board(board)`**:
    -   Выводит текущее состояние игрового поля в консоль. Нумерация строк и столбцов для удобства.

3.  **Функция `check_winner(board, player)`**:
    -   Проверяет, есть ли победитель.
    -   Символ текущего игрока ('X' для игрока 1, 'O' для игрока 2).
    -   Проверяет горизонтальные, вертикальные и обе диагональные линии на наличие пяти подряд идущих символов.
    -   Возвращает `True`, если победитель найден, иначе `False`.

4. **Функция `check_full_board(board)`**:
    - Проверяет, заполнено ли игровое поле.
    - Возвращает `True`, если нет пустых клеток, иначе `False`.

5.  **Основной цикл игры `while game_on:`**:
    -   Продолжается, пока `game_on` равно `True`.
    -   Выводит текущую доску.
    -   **Ход игрока**:
        -   Если `current_player` равен 1, то это ход первого игрока.
        -   Запрашивает ввод координат x и y.
         -   Проверяет, что координаты в допустимых пределах и ячейка пуста. Если нет, повторяет запрос.
        -   Устанавливает символ 'X' в выбранную ячейку.
        -   Переключает текущего игрока на второго (`current_player = 2`).
    -   **Ход компьютера**:
        -   Если `current_player` равен 2, то это ход компьютера.
        -   Компьютер выбирает случайные координаты x и y.
        -   Проверяет, что ячейка не занята.
        -   Устанавливает символ 'O' в выбранную ячейку.
        -   Переключает текущего игрока на первого (`current_player = 1`).
    -   **Проверка на победу или ничью**:
        -   Вызывает `check_winner()` для проверки наличия победителя, и если он есть выводит на консоль сообщение о победе, и устанавливает `game_on` в `False`.
        -   Вызывает `check_full_board()` для проверки, заполнено ли поле. Если поле заполнено, то выводит сообщение о ничьей и завершает игру.

"""
```