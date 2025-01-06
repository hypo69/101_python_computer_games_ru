### Название игры: **QUBIC** (Кубик)

---

#### Описание  
**QUBIC** — это трёхмерная версия игры "Крестики-нолики". Игроки по очереди ставят свои символы (крестики или нолики) на кубе размером 4x4x4. Цель игры — первым создать линию из четырёх своих символов в любом направлении (горизонтальном, вертикальном или диагональном) на одном из уровней, столбцов или диагоналей куба.

---

### Пошаговая инструкция для реализации

#### 1. **Инициализация игры**
   - Программа выводит приветственное сообщение и объясняет правила:  
     ```
     Добро пожаловать в QUBIC!  
     Ваша задача — первым создать линию из четырёх своих символов на кубе 4x4x4.  
     Игра продолжается до тех пор, пока один из игроков не создаст линию или пока не будет заполнен весь куб.  
     Удачи!  
     ```

   - Программа создаёт трёхмерный куб размером 4x4x4, где каждая ячейка изначально пуста.  
   - Игроки поочерёдно делают ходы, ставя свои символы (крестики или нолики) на кубе.

---

#### 2. **Основной процесс игры**

##### **2.1. Ход игрока:**
   - Игрок выбирает координаты (X, Y, Z) для размещения своего символа.  
   - Программа проверяет, является ли ячейка свободной:  
     - Если ячейка свободна, символ игрока размещается в этой ячейке.  
     - Если ячейка уже занята, программа сообщает об ошибке и предлагает игроку повторить ход:  
       ```
       Ячейка уже занята. Попробуйте снова.  
       ```

   - Программа отображает текущее состояние куба:  
     ```
     Текущее состояние куба:  
     Уровень 1:  
     [X][ ][ ][ ]  
     [ ][O][ ][ ]  
     [ ][ ][X][ ]  
     [ ][ ][ ][O]  
     ```

##### **2.2. Проверка условий победы:**
   - После каждого хода программа проверяет, создал ли игрок линию из четырёх своих символов:  
     - В горизонтальном направлении на одном уровне.  
     - В вертикальном направлении в одном столбце.  
     - В диагональном направлении на одном уровне или через уровни.  

   - Если игрок создал линию, программа объявляет его победителем:  
     ```
     Игра окончена! Победил Игрок 1.  
     ```

##### **2.3. Проверка условий завершения игры:**
   - Игра заканчивается, если весь куб заполнен, и ни один игрок не создал линию.  
   - Программа объявляет ничью:  
     ```
     Игра окончена! Ничья.  
     ```

---

#### 3. **Завершение игры**
   - После завершения игры программа предлагает сыграть снова:  
     ```
     Хотите сыграть снова? (да/нет)  
     ```

   - Если игрок выбирает "да", игра начинается заново с нового куба.  

---

### Пример работы программы

1. **Начало игры:**  
   ```  
   Добро пожаловать в QUBIC!  
   Игрок 1, ваш ход.  
   Введите координаты (X, Y, Z) для размещения символа (от 1 до 4):  
   > 1, 1, 1  
   Символ X размещён в ячейке (1, 1, 1).  
   ```

2. **Игровой процесс:**  
   ```  
   Игрок 2, ваш ход.  
   Введите координаты (X, Y, Z) для размещения символа:  
   > 2, 2, 2  
   Символ O размещён в ячейке (2, 2, 2).  

   Игрок 1, ваш ход.  
   Введите координаты (X, Y, Z) для размещения символа:  
   > 3, 3, 3  
   Символ X размещён в ячейке (3, 3, 3).  
   ```

3. **Завершение игры:**  
   ```  
   Игра окончена! Победил Игрок 1.  
   Хотите сыграть снова? (да/нет):  
   > нет  
   Спасибо за игру!  
   ```

---

### Возможные ограничения  
- Игрок должен вводить координаты в правильном диапазоне (от 1 до 4).  
- Программа должна обрабатывать неверный ввод и предлагать повторить попытку.  
- Ячейки не могут быть заняты повторно.

---

### Реализация  
Игра может быть реализована на Python с использованием следующих возможностей:  
- **Трёхмерные массивы** для представления куба и его состояния.  
- **Циклы и условия** для проверки ввода игрока и обработки его ходов.  
- **Функции** для проверки условий победы и завершения игры.  

---

### Рекомендуемые улучшения  
- Добавить возможность игры с компьютером.  
- Реализовать графический интерфейс для визуализации куба и ходов.  
- Добавить возможность выбора размера куба (например, 3x3x3 или 5x5x5).