### Название игры: **ROCKET** (Ракета)

---

#### Описание  
**ROCKET** — это стратегическая игра, в которой игроки управляют космическими кораблями (ракетами), стремясь первыми достичь цели — орбиты планеты. Игроки по очереди перемещают свои ракеты по сетке, избегая препятствий и пытаясь опередить соперника. Игра заканчивается, когда один из игроков достигает орбиты планеты.

---

### Пошаговая инструкция для реализации

#### 1. **Инициализация игры**
   - Программа выводит приветственное сообщение и объясняет правила:  
     ```
     Добро пожаловать в ROCKET!  
     Ваша задача — первым достичь орбиты планеты, перемещая свою ракету по сетке.  
     Игра продолжается до тех пор, пока один из игроков не достигнет орбиты или пока не будет достигнуто максимальное количество ходов.  
     Удачи!  
     ```

   - Программа создаёт игровую сетку размером 10x10.  
   - Ракеты двух игроков размещаются на противоположных концах сетки (например, ракета Игрока 1 на клетке A1, а ракета Игрока 2 на клетке J10).  
   - На сетке случайным образом размещаются препятствия (например, астероиды), которые нельзя пересекать.  
   - Игроки поочерёдно делают ходы, перемещая свои ракеты.

---

#### 2. **Основной процесс игры**

##### **2.1. Ход игрока:**
   - Игрок выбирает направление и количество клеток, на которое хочет переместить свою ракету (например, вверх на 2 клетки).  
   - Программа проверяет, является ли ход допустимым:  
     - Ракета не может перемещаться за пределы сетки.  
     - Ракета не может перемещаться на клетку с препятствием.  
     - Ракета не может перемещаться на клетку, занятую ракетой соперника.

   - Если ход допустим, программа перемещает ракету и отображает текущее состояние сетки:  
     ```
     Текущее состояние сетки:  
     A B C D E F G H I J  
     1 [R][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
     2 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
     3 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
     4 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
     5 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
     6 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
     7 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
     8 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
     9 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
    10 [ ][ ][ ][ ][ ][ ][ ][ ][ ][R]  
     ```

   - Если ход недопустим, программа сообщает об ошибке и предлагает игроку повторить ход:  
     ```
     Недопустимый ход. Попробуйте снова.  
     ```

##### **2.2. Проверка условий победы:**
   - После каждого хода программа проверяет, достигла ли ракета игрока орбиты планеты.  
   - Если ракета достигла орбиты, программа объявляет победителя:  
     ```
     Игра окончена! Победил Игрок 1.  
     ```

##### **2.3. Проверка условий завершения игры:**
   - Игра заканчивается, если достигнуто максимальное количество ходов (например, 20 ходов).  
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

   - Если игрок выбирает "да", игра начинается заново с новой расстановкой ракет и препятствий.  

---

### Пример работы программы

1. **Начало игры:**  
   ```  
   Добро пожаловать в ROCKET!  
   Игрок 1, ваш ход.  
   Введите направление и количество клеток для перемещения ракеты (например, вверх 2):  
   > вверх 2  
   Ракета Игрока 1 перемещена на клетку A3.  
   ```

2. **Игровой процесс:**  
   ```  
   Игрок 2, ваш ход.  
   Введите направление и количество клеток для перемещения ракеты:  
   > вниз 1  
   Ракета Игрока 2 перемещена на клетку J9.  

   Игрок 1, ваш ход.  
   Введите направление и количество клеток для перемещения ракеты:  
   > вправо 3  
   Ракета Игрока 1 перемещена на клетку D3.  
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
- Игрок должен вводить направление и количество клеток в правильном формате.  
- Программа должна обрабатывать неверный ввод и предлагать повторить попытку.  
- Ракеты не могут перемещаться за пределы сетки или на клетки с препятствиями.

---

### Реализация  
Игра может быть реализована на Python с использованием следующих возможностей:  
- **Массивы или списки** для представления сетки и положения ракет.  
- **Циклы и условия** для проверки ввода игрока и обработки его ходов.  
- **Функции** для проверки условий победы и завершения игры.  

---

### Рекомендуемые улучшения  
- Добавить возможность игры с компьютером.  
- Реализовать графический интерфейс для визуализации сетки и ходов.  
- Добавить возможность выбора размера сетки (например, 8x8 или 12x12).