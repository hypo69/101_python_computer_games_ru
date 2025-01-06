### Название игры: **CALNDR** (Перпетуальный календарь)

#### Описание
**CALNDR** — это программа, которая позволяет пользователю вывести календарь для любого года. Чтобы использовать программу, необходимо указать день недели, с которого начинается год. Для этого используется программа **WEKDAY**. Вводя правильное число для дня недели, вы можете получить точный календарь для выбранного года. Вы также можете адаптировать программу под високосные годы, внося изменения в код программы.

---

### Пошаговая инструкция для реализации

#### 1. **Инициализация игры**
   - Программа запрашивает ввод года и дня недели, с которого он начинается.
   - Дни недели кодируются как числа:
     - 0 — воскресенье
     - -1 — понедельник
     - -2 — вторник
     - и так далее.
   - Чтобы получить правильное начало года, воспользуйтесь функцией **WEKDAY** для вычисления дня недели для 1 января того года.

#### 2. **Основной цикл игры**
   - **Ввод данных:**
     1. Программа запрашивает ввод года.
     2. Затем пользователю нужно ввести число, которое соответствует началу года (например, 0 для воскресенья).
   - **Вывод календаря:**
     Программа будет поочередно выводить календарь для каждого месяца выбранного года. Каждый месяц будет отображаться с номерами дней недели и днями месяца.

#### 3. **Подсчёт победителя**
   - Игра не имеет победителя, так как цель игры — корректно вывести календарь для заданного года.

#### 4. **Завершение игры**
   - После того как календарь будет выведен, программа предложит пользователю продолжить или завершить игру:
     ```
     Хотите вывести календарь для другого года? (да/нет)
     ```

---

### Пример работы программы

1. **Начало игры:**
   ```
   Добро пожаловать в программу CALNDR!
   Введите год: 2024
   Введите день недели, с которого начинается год (0 - воскресенье, -1 - понедельник и т.д.): -1
   ```

2. **Вывод календаря:**
   ```
   Январь 2024
   Пн Вт Ср Чт Пт Сб Вс
   1  2  3  4  5  6  7
   8  9 10 11 12 13 14
   15 16 17 18 19 20 21
   22 23 24 25 26 27 28
   29 30 31
   ```

3. **Завершение игры:**
   ```
   Хотите вывести календарь для другого года? (да/нет)
   > нет
   Спасибо за использование программы!
   ```

---

### Возможные ограничения
- Программа требует корректного ввода года и дня недели, иначе она может не работать.
- Для високосных лет необходимо вручную внести изменения в код программы (например, для февраля).

---

### Реализация
Игра реализована с помощью базовых вычислений, чтобы вывести календарь для любого года на основе информации о днях недели и количестве дней в месяце.