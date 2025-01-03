### Название игры: **LETTER** (Угадай букву)

---

#### Описание  
**LETTER** — это игра, в которой программа загадывает случайную букву алфавита, а игрок должен угадать её за минимальное количество попыток. После каждого ввода программа даёт подсказки, указывая, находится ли загаданная буква "выше" или "ниже" по алфавиту относительно введённой игроком.

---

### Пошаговая инструкция для реализации

#### 1. **Инициализация игры**  
   - При запуске игры программа приветствует пользователя и объясняет правила:
     ```
     Добро пожаловать в игру LETTER!  
     Я загадаю одну букву алфавита от A до Z.  
     Ваша задача — угадать её, используя мои подсказки.  
     После каждого предположения я скажу, выше или ниже ваша буква по алфавиту.  
     Удачи!  
     ```

   - Программа случайным образом выбирает одну букву алфавита (A–Z) для угадывания.

#### 2. **Основной процесс игры**
   - **Ввод игрока:**
     1. Игрок вводит свою догадку (букву от A до Z).  
     2. Программа сравнивает введённую букву с загаданной:
        - Если введённая буква меньше загаданной по алфавиту, программа отвечает: "Загаданная буква выше по алфавиту."
        - Если введённая буква больше загаданной по алфавиту, программа отвечает: "Загаданная буква ниже по алфавиту."
        - Если игрок угадал, программа поздравляет его с победой.

   - **Количество попыток:**
     - Игрок может делать неограниченное количество попыток, пока не угадает загаданную букву.

   - **Подсказки:**
     - Каждая подсказка помогает игроку сужать диапазон возможных букв.

#### 3. **Завершение игры**
   - Когда игрок угадывает загаданную букву, программа выводит поздравительное сообщение:
     ```
     Поздравляем! Вы угадали букву за X попыток!  
     Хотите сыграть снова? (да/нет)
     ```

   - Если игрок выбирает "да", начинается новый раунд с новой загаданной буквой.  
   - Если игрок выбирает "нет", программа завершает игру:
     ```
     Спасибо за игру! До встречи!
     ```

---

### Пример работы программы

1. **Начало игры:**  
   ```  
   Добро пожаловать в игру LETTER!  
   Я загадал букву алфавита от A до Z. Угадайте её.  
   Введите букву:  
   > M  
   Загаданная буква выше по алфавиту.  
   Введите букву:  
   > S  
   Загаданная буква ниже по алфавиту.  
   Введите букву:  
   > P  
   Поздравляем! Вы угадали букву за 3 попытки!  
   Хотите сыграть снова? (да/нет):  
   > нет  
   Спасибо за игру!  
   ```

---

### Возможные ограничения  
- Игрок может вводить только одну букву за раз.  
- Программа должна обрабатывать ввод и выводить сообщение об ошибке, если введён некорректный символ (например, цифра или более одной буквы).  
- Загаданные буквы должны быть только в верхнем регистре (A–Z).

---

### Реализация  
Игра может быть реализована на Python с использованием следующих возможностей:  
- **Модуль `random`** для генерации случайной буквы.  
- **Циклы и условия** для обработки ввода игрока и проверки его догадок.  
- Логика подсказок для определения, выше или ниже буква по алфавиту.

Рекомендуется:  
- Добавить возможность выбора диапазона букв (например, A–M или N–Z) для увеличения сложности.  
- Добавить таблицу лидеров с отображением минимального количества попыток для угадывания буквы.  