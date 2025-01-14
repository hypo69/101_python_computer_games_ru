### Название игры: **CIVILW** (Гражданская война)

#### Описание
**CIVILW** — это симуляция сражений Гражданской войны США. Игра основана на 14 реальных сражениях, используя факты и цифры из исторических событий. Задача игрока — управлять армией, принимая стратегические решения, такие как выбор оборонительной и наступательной тактики. Суть игры заключается в том, чтобы правильно реагировать на действия противника и проводить успешные операции, опираясь на историческую стратегию.

---

### Пошаговая инструкция для реализации

#### 1. **Инициализация игры**
   - Программа начинает с выбора сражения, например, Битва при Булл-Ран или Шилох.
   - Игрок управляет армией конфедератов, а компьютер — армией Союза. Задача — правильно реагировать на вражеские действия и победить в сражении.

#### 2. **Основной цикл игры**
   - **Ввод данных:**
     1. Игроку предлагаются различные стратегические опции для выбора:
        - **Оборонительные стратегии:**
          - Артиллерийская атака
          - Укрепления против фронтальных атак
          - Укрепления против фланговых маневров
          - Отступление
        - **Наступательные стратегии:**
          - Артиллерийская атака
          - Прямой удар
          - Маневры по флангу
          - Окружение
     2. Игрок выбирает одну из этих стратегий в ответ на вражеские действия.
     3. После каждого сражения игроку сообщается, сколько потерь понесли его войска по сравнению с реальными потерями в битве.

#### 3. **Подсчёт победителя**
   - Игра продолжается до тех пор, пока одна из сторон не одержит победу в сражении.
   - Если у игрока больше потерь, чем у компьютера, он проигрывает.
   - После каждой битвы игроку сообщается, выиграл ли он или проиграл, в зависимости от успешности стратегии.

#### 4. **Завершение игры**
   - После того как игрок завершит все сражения или проиграет, программа предложит сыграть снова:
     ```
     Хотите сыграть снова? (да/нет)
     ```

---

### Пример работы программы

1. **Начало игры:**
   ```
   Добро пожаловать в игру CIVILW!
   Вы — командующий армией Конфедерации. Битва начинается.
   Выберите стратегию:
   1. Артиллерийская атака
   2. Укрепления против фронтальной атаки
   3. Укрепления против фланговых маневров
   4. Отступление
   > 1
   ```

2. **После сражения:**
   ```
   Ваша стратегия была успешной! Потери: 500 человек.
   Потери противника: 700 человек.
   Вы выиграли сражение.
   ```

3. **Завершение игры:**
   ```
   Хотите сыграть снова? (да/нет)
   > нет
   Спасибо за игру!
   ```

---

### Возможные ограничения
- Игра основывается на исторических фактах, и результат сражений может быть предсказуем, если следовать историческим стратегиям.
- Программа не поддерживает сложные изменения в стратегии, и решения должны соответствовать реальным историческим событиям.

---

### Реализация
Игра реализована с помощью текстового ввода, где игрок выбирает стратегические опции, а программа определяет исход сражения на основе этих выборов.