### Название игры: **STOCK** (Акции)

---

#### Описание  
**STOCK** — это игра, в которой игрок управляет портфелем акций, покупая и продавая акции на основе прогнозов рынка. Цель игры — максимизировать прибыль, покупая акции по низкой цене и продавая их по высокой. Игра продолжается в течение определённого количества дней, и игрок должен делать выборы, основываясь на прогнозах цен на акции.

---

### Пошаговая инструкция для реализации

#### 1. **Инициализация игры**
   - Программа выводит приветственное сообщение и объясняет правила:  
     ```
     Добро пожаловать в STOCK!  
     Ваша задача — управлять портфелем акций, покупая и продавая акции на основе прогнозов рынка.  
     Цель игры — максимизировать прибыль, покупая акции по низкой цене и продавая их по высокой.  
     Игра продолжается в течение 10 дней.  
     Удачи!  
     ```

   - Программа создаёт список акций с их начальными ценами.  
   - Игрок начинает с определённым количеством денег (например, $1000).  
   - Игрок поочерёдно делает выборы: покупать, продавать или ничего не делать.

---

#### 2. **Основной процесс игры**

##### **2.1. Ход игрока:**
   - Программа отображает текущие цены на акции и предлагает игроку выбрать действие:  
     ```
     День 1:  
     Акции компании A: $50  
     Акции компании B: $30  
     Акции компании C: $70  
     Ваш баланс: $1000  
     Ваши акции:  
     Компания A: 0  
     Компания B: 0  
     Компания C: 0  

     Выберите действие:  
     1. Купить акции  
     2. Продать акции  
     3. Ничего не делать  
     ```

   - Игрок выбирает действие и указывает количество акций для покупки или продажи.  
   - Программа проверяет, достаточно ли у игрока денег или акций для совершения операции:  
     - Если операция возможна, программа обновляет баланс и количество акций.  
     - Если операция невозможна, программа сообщает об ошибке и предлагает игроку повторить выбор:  
       ```
       Недостаточно денег для покупки. Попробуйте снова.  
       ```

##### **2.2. Обновление цен на акции:**
   - После каждого хода программа случайным образом обновляет цены на акции.  
   - Программа сообщает новые цены на акции:  
     ```
     День 2:  
     Акции компании A: $55  
     Акции компании B: $28  
     Акции компании C: $72  
     ```

##### **2.3. Проверка условий завершения игры:**
   - Игра заканчивается после 10 дней.  
   - Программа подсчитывает итоговый баланс игрока, включая стоимость всех акций:  
     ```
     Игра окончена!  
     Ваш итоговый баланс: $1200  
     ```

---

#### 3. **Завершение игры**
   - После завершения игры программа предлагает сыграть снова:  
     ```
     Хотите сыграть снова? (да/нет)  
     ```

   - Если игрок выбирает "да", игра начинается заново с новыми начальными ценами на акции.  

---

### Пример работы программы

1. **Начало игры:**  
   ```  
   Добро пожаловать в STOCK!  
   День 1:  
   Акции компании A: $50  
   Акции компании B: $30  
   Акции компании C: $70  
   Ваш баланс: $1000  
   Ваши акции:  
   Компания A: 0  
   Компания B: 0  
   Компания C: 0  

   Выберите действие:  
   1. Купить акции  
   2. Продать акции  
   3. Ничего не делать  
   > 1  
   Введите количество акций компании A для покупки:  
   > 10  
   ```

2. **Игровой процесс:**  
   ```  
   День 2:  
   Акции компании A: $55  
   Акции компании B: $28  
   Акции компании C: $72  
   Ваш баланс: $450  
   Ваши акции:  
   Компания A: 10  
   Компания B: 0  
   Компания C: 0  

   Выберите действие:  
   1. Купить акции  
   2. Продать акции  
   3. Ничего не делать  
   > 2  
   Введите количество акций компании A для продажи:  
   > 5  
   ```

3. **Завершение игры:**  
   ```  
   Игра окончена!  
   Ваш итоговый баланс: $1200  
   Хотите сыграть снова? (да/нет):  
   > нет  
   Спасибо за игру!  
   ```

---

### Возможные ограничения  
- Игрок должен вводить количество акций в правильном формате.  
- Программа должна обрабатывать неверный ввод и предлагать повторить попытку.  
- Игрок не может покупать или продавать акции, если у него недостаточно денег или акций.

---

### Реализация  
Игра может быть реализована на Python с использованием следующих возможностей:  
- **Модуль `random`** для генерации случайных цен на акции.  
- **Циклы и условия** для проверки ввода игрока и обработки его ходов.  
- **Функции** для обновления баланса и количества акций.  

---

### Рекомендуемые улучшения  
- Добавить возможность выбора количества дней (например, 5 или 15).  
- Реализовать графический интерфейс для визуализации цен на акции и баланса.  
- Добавить возможность игры с несколькими игроками.