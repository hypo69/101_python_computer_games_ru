### Название игры: **SPACWR** (Космический корабль)

---

#### Описание  
**SPACWR** — это игра, в которой игрок управляет космическим кораблём, пытаясь избежать столкновения с астероидами. Игрок по очереди выбирает направление движения корабля, чтобы избежать столкновения. Цель игры — продержаться как можно дольше, избегая столкновений с астероидами.

---

### Пошаговая инструкция для реализации

#### 1. **Инициализация игры**
   - Программа выводит приветственное сообщение и объясняет правила:  
     ```
     Добро пожаловать в SPACWR!  
     Ваша задача — управлять космическим кораблём, избегая столкновения с астероидами.  
     Игра продолжается до тех пор, пока вы не столкнётесь с астероидом.  
     Удачи!  
     ```

   - Программа создаёт игровую сетку размером 10x10.  
   - Космический корабль размещается в центре сетки.  
   - Астероиды случайным образом появляются на краях сетки и движутся к центру.  
   - Игрок поочерёдно выбирает направление движения корабля.

---

#### 2. **Основной процесс игры**

##### **2.1. Ход игрока:**
   - Игрок выбирает направление движения корабля (например, вверх, вниз, влево, вправо).  
   - Программа проверяет, является ли ход допустимым:  
     - Корабль не может выйти за пределы сетки.  
     - Корабль не может перемещаться на клетку с астероидом.

   - Если ход допустим, программа перемещает корабль и отображает текущее состояние сетки:  
     ```
     Текущее состояние сетки:  
     A B C D E F G H I J  
     1 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
     2 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
     3 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
     4 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
     5 [ ][ ][ ][ ][R][ ][ ][ ][ ][ ]  
     6 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
     7 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
     8 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
     9 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
    10 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
     ```

   - Если ход недопустим, программа сообщает об ошибке и предлагает игроку повторить ход:  
     ```
     Недопустимый ход. Попробуйте снова.  
     ```

##### **2.2. Движение астероидов:**
   - После каждого хода игрока программа перемещает астероиды к центру сетки.  
   - Программа проверяет, произошло ли столкновение корабля с астероидом:  
     - Если столкновение произошло, программа объявляет проигрыш:  
       ```
       Столкновение! Ваш корабль уничтожен.  
       ```
     - Если столкновения не произошло, игра продолжается.

##### **2.3. Проверка условий завершения игры:**
   - Игра заканчивается, когда корабль сталкивается с астероидом.  
   - Программа объявляет итоговое количество ходов:  
     ```
     Игра окончена! Вы продержались 15 ходов.  
     ```

---

#### 3. **Завершение игры**
   - После завершения игры программа предлагает сыграть снова:  
     ```
     Хотите сыграть снова? (да/нет)  
     ```

   - Если игрок выбирает "да", игра начинается заново с новой расстановкой астероидов.  

---

### Пример работы программы

1. **Начало игры:**  
   ```  
   Добро пожаловать в SPACWR!  
   Ваша задача — управлять космическим кораблём, избегая столкновения с астероидами.  
   Введите направление движения корабля (вверх, вниз, влево, вправо):  
   > вверх  
   Корабль перемещён на клетку A5.  
   ```

2. **Игровой процесс:**  
   ```  
   Текущее состояние сетки:  
   A B C D E F G H I J  
   1 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
   2 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
   3 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
   4 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
   5 [R][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
   6 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
   7 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
   8 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
   9 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  
  10 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]  

   Введите направление движения корабля:  
   > вправо  
   Корабль перемещён на клетку B5.  
   ```

3. **Завершение игры:**  
   ```  
   Столкновение! Ваш корабль уничтожен.  
   Игра окончена! Вы продержались 15 ходов.  
   Хотите сыграть снова? (да/нет):  
   > нет  
   Спасибо за игру!  
   ```

---

### Возможные ограничения  
- Игрок должен вводить направление движения в правильном формате.  
- Программа должна обрабатывать неверный ввод и предлагать повторить попытку.  
- Корабль не может перемещаться за пределы сетки или на клетку с астероидом.

---

### Реализация  
Игра может быть реализована на Python с использованием следующих возможностей:  
- **Массивы или списки** для представления сетки и положения корабля и астероидов.  
- **Циклы и условия** для проверки ввода игрока и обработки его ходов.  
- **Функции** для проверки столкновений и обновления состояния сетки.  

---

### Рекомендуемые улучшения  
- Добавить возможность выбора уровня сложности (например, увеличение количества астероидов).  
- Реализовать графический интерфейс для визуализации сетки и движения корабля.  
- Добавить возможность выбора размера сетки (например, 8x8 или 12x12).