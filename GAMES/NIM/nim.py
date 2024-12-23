```
NIM:
=================
Сложность: 5
-----------------
Игра "NIM" - это математическая игра для двух игроков. В начале игры есть несколько кучек камней (или других предметов). Игроки по очереди берут любое количество камней из одной кучки. Выигрывает игрок, взявший последний камень.

Правила игры:
1.  В начале игры есть несколько кучек камней, количество камней в каждой кучке задается.
2.  Игроки по очереди берут любое ненулевое количество камней из одной кучки.
3.  Игрок, который берет последний камень, выигрывает.
-----------------
Алгоритм:
1.  Инициализировать кучки камней (массив `P`).
2.  Показать текущее состояние кучек камней.
3.  Начать игровой цикл, пока сумма всех камней в кучках больше 0.
4.  Запросить у текущего игрока (человека или компьютера) номер кучки и количество камней для взятия.
    4.1 Проверить корректность ввода, номер кучки должен быть в пределах допустимых значений, и количество камней не должно превышать текущее количество в выбранной кучке.
5.  Вычесть выбранное количество камней из выбранной кучки.
6.  Показать текущее состояние кучек камней.
7.  Переключить ход на следующего игрока.
8.  Когда сумма всех камней равна 0, определить и объявить победителя.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializePiles["<p align='left'>Инициализация кучек:
    <code><b>
    piles = [random(1,10),random(1,10),random(1,10)]
    turn = 0
    </b></code></p>"]
    InitializePiles --> DisplayPiles["Отображение кучек"]
    DisplayPiles --> GameLoopStart{"Начало цикла игры: пока есть камни"}
    GameLoopStart -- Да --> GetInput["<p align='left'>Ввод игрока:
    <code><b>
    pileNumber
    stonesToRemove
    </b></code></p>"]
    GetInput --> ValidateInput{"<p align='left'>Проверка ввода:
    <code><b>
    pileNumber valid?
    stonesToRemove valid?
    </b></code></p>"}
    ValidateInput -- Да --> UpdatePiles["<code><b>piles[pileNumber] -= stonesToRemove</b></code>"]
    UpdatePiles --> DisplayPiles2["Отображение кучек"]
    DisplayPiles2 --> SwitchPlayer["<code><b>turn = (turn + 1) % 2</b></code>"]
    SwitchPlayer --> GameLoopStart
    ValidateInput -- Нет --> OutputError["Вывод ошибки ввода"]
    OutputError --> GetInput
    GameLoopStart -- Нет --> DetermineWinner["Определение победителя"]
    DetermineWinner --> OutputWinner["Вывод победителя"]
    OutputWinner --> End["Конец"]
```
Legenda:
    Start - Начало игры.
    InitializePiles - Инициализация кучек камней (piles) случайными значениями от 1 до 10 и установка первого хода (turn) в 0 (игрок 1).
    DisplayPiles - Отображение текущего состояния кучек камней.
    GameLoopStart - Начало основного игрового цикла. Цикл продолжается, пока есть хотя бы один камень в кучках.
    GetInput - Запрос ввода от игрока номера кучки (pileNumber) и количества камней для удаления (stonesToRemove).
    ValidateInput - Проверка корректности ввода: убедиться, что номер кучки и количество камней допустимы.
    UpdatePiles - Обновление состояния кучек, вычитание выбранного количества камней из выбранной кучки.
    DisplayPiles2 - Отображение обновленного состояния кучек.
    SwitchPlayer - Переключение хода между игроками (игрок 1 и игрок 2).
    OutputError - Вывод сообщения об ошибке ввода, если ввод не корректен.
     DetermineWinner - Определение победителя после окончания игры.
    OutputWinner - Вывод сообщения о победе соответствующего игрока.
    End - Конец игры.
"""
import random

# Функция для отображения кучек камней
def display_piles(piles):
    """
    Выводит текущее состояние кучек камней.
    
    Args:
    piles (list): Список, представляющий кучки камней.
    """
    print("Текущее состояние кучек:")
    for i, pile in enumerate(piles):
        print(f"Кучка {i + 1}: {pile} камней")
# Функция для хода игрока
def get_player_move(piles, player):
        """
        Запрашивает у игрока номер кучки и количество камней для удаления.
        
        Args:
            piles (list): Список, представляющий кучки камней.
            player (int): Номер текущего игрока (1 или 2).

        Returns:
            tuple: Кортеж, содержащий номер кучки и количество камней для удаления.
        """

        while True:
            try:
                pile_number = int(input(f"Игрок {player}, выберите номер кучки (1-{len(piles)}): ")) - 1
                if 0 <= pile_number < len(piles):
                    stones_to_remove = int(input(f"Игрок {player}, сколько камней взять из кучки {pile_number + 1}: "))
                    if 0 < stones_to_remove <= piles[pile_number]:
                        return pile_number, stones_to_remove
                    else:
                        print("Недопустимое количество камней. Пожалуйста, выберите значение от 1 до текущего количества в кучке.")
                else:
                    print("Недопустимый номер кучки. Пожалуйста, выберите существующую кучку.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите целые числа.")
# Основная функция игры
def play_nim():
    """
    Реализует игру NIM.
    """
    # Инициализация кучек камней
    piles = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    current_player = 0  # 0 - игрок 1, 1 - игрок 2
    
    # Игровой цикл
    while sum(piles) > 0:
        display_piles(piles)
        # Ход текущего игрока
        pile_number, stones_to_remove = get_player_move(piles, current_player + 1)
        piles[pile_number] -= stones_to_remove
        current_player = (current_player + 1) % 2 # Переключение игрока
    # Определение победителя
    print(f"Игрок {current_player + 1} победил!")

# Запуск игры
if __name__ == "__main__":
    play_nim()
"""
Объяснение кода:

1.  **Импорт модуля `random`**:
    -   `import random`: Импортирует модуль `random`, который используется для генерации случайных чисел (количества камней в кучках).
2. **Функция `display_piles(piles)`**:
    -   Принимает список `piles`, представляющий кучки камней.
    -   Выводит на экран текущее состояние каждой кучки, используя `enumerate` для отображения номера кучки и количества камней в ней.
3. **Функция `get_player_move(piles, player)`**:
     - Запрашивает у текущего игрока `player` номер кучки и количество камней для удаления.
    -  Проверяет корректность ввода:
        -   Номер кучки должен быть в пределах допустимых значений (от 1 до количества кучек).
        -   Количество камней должно быть больше нуля и не превышать количество камней в выбранной кучке.
    -  Возвращает номер кучки (с индексом, начиная с 0) и количество камней для удаления.
4. **Функция `play_nim()`**:
    -   Инициализирует три кучки камней случайными значениями от 1 до 10.
    -   `current_player = 0`: Устанавливает первого игрока (игрок 1).
    -  Основной игровой цикл `while sum(piles) > 0`: продолжается, пока есть камни в кучках.
    -   Вызывает `display_piles()` для отображения текущего состояния кучек.
    -   Вызывает `get_player_move()` для получения хода текущего игрока.
    -   Обновляет количество камней в выбранной кучке.
    -   Переключает игрока `current_player = (current_player + 1) % 2` (0 -> 1, 1 -> 0).
    -   После завершения цикла (когда все камни забраны) объявляет победителя.
5.  **Запуск игры**:
    -   `if __name__ == "__main__":`:  Гарантирует, что игра запустится, только если скрипт запущен напрямую.
    -   `play_nim()`: Вызывает функцию для начала игры.
"""
