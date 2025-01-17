### Название игры: **HANG** (Виселица)

---

#### Описание  
**HANG** — это классическая игра "Виселица", в которой игрок должен угадать слово, угадывая по очереди буквы. За каждую неправильную букву добавляется часть висельника, и игрок теряет попытки. Если игрок угадает все буквы слова до того, как висельник будет полностью собран, он выигрывает. Если висельник собран полностью (ошибки превышают допустимое количество), игрок проигрывает.

---

### Пошаговая инструкция для реализации

#### 1. **Инициализация игры**  
   - При запуске игры программа приветствует пользователя и объясняет правила.  
   - Программа выбирает случайное слово из заранее заданного списка.  
   - Игроку предоставляется 6 попыток (или другое количество) для угадывания слова.  
   - Программа отображает количество букв в слове в виде подчеркиваний (например, "_ _ _ _ _").

#### 2. **Основной процесс игры**
   - **Угадывание букв:**
     1. Игрок поочередно вводит буквы, пытаясь угадать слово.
     2. Если буква присутствует в слове, она открывается в соответствующих позициях.
     3. Если буква не присутствует в слове, программа добавляет одну деталь висельника.
   
   - **Ошибки:**  
     1. Игрок может совершить не более 6 ошибок (или другое количество, в зависимости от сложности).
     2. За каждую неправильную букву добавляется один элемент к висельнику.
   
   - **Проверка выигрыша или проигрыша:**
     1. Если игрок угадывает все буквы слова до того, как висельник будет полностью собран, он выигрывает.
     2. Если количество ошибок превышает допустимое, игрок проигрывает.

#### 3. **Подсчёт попыток и ошибок**
   - Программа отслеживает количество оставшихся попыток.  
   - Игрок должен угадывать буквы, пока не угадано всё слово или пока не исчерпаны все попытки.

#### 4. **Завершение игры**
   - Когда игрок выигрывает или проигрывает, программа сообщает результат и предлагает сыграть снова:
     ```  
     Поздравляем! Вы угадали слово!
     Хотите сыграть снова? (да/нет)
     ```

   - Если игрок выбирает "да", начинается новый раунд с новым словом.  
   - Если "нет", программа завершает работу.

---

### Пример работы программы  

1. **Начало игры:**  
   ```  
   Добро пожаловать в игру HANG!  
   Угадайте слово. У вас 6 попыток.  
   Загаданное слово: _ _ _ _ _  
   ```  

2. **Игровой процесс:**  
   ```  
   Введите букву:  
   > а  
   Буква "а" есть в слове: _ а _ _ _  
   У вас 6 попыток.  

   Введите букву:  
   > б  
   Буквы "б" нет в слове.  
   Осталось попыток: 5  
   У вас 5 попыток.  

   Введите букву:  
   > р  
   Буква "р" есть в слове: р а _ _ _  
   У вас 5 попыток.  
   ```  

3. **Результат игры:**  
   ```  
   Поздравляем! Вы угадали слово "рамка" за 4 попытки!  
   Хотите сыграть снова? (да/нет):  
   > нет  
   Спасибо за игру!  
   ```  

---

### Возможные ограничения  
- Слово должно быть ограничено заранее определённым списком.
- Игрок может сделать не более 6 ошибок.
- Программа должна учитывать только одну букву за раз и обрабатывать повторяющиеся буквы.

---

### Реализация  
Игра может быть реализована на Python с использованием следующих возможностей:  
- **Модуль `random`** для случайного выбора слова из списка.  
- **Циклы и условия** для обработки ввода игрока, отслеживания ошибок и отображения состояния игры.
- **Текстовая визуализация** висельника с каждым неверным шагом (например, строки для частей тела висельника).

Рекомендуется:  
- Реализовать графическую версию для визуализации висельника.
- Добавить разные уровни сложности с разной длиной слов и количеством попыток.