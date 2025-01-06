### Название игры: **HMRABI** (Игра с числами)

---

#### Описание  
**HMRABI** — это логическая игра, в которой игрок должен угадать загаданное число, используя подсказки программы. В процессе игры игрок вводит числа и получает подсказку, указывающую на то, насколько близким является введённое число к загаданному. Цель игры — угадать число за минимальное количество попыток.

---

### Пошаговая инструкция для реализации

#### 1. **Инициализация игры**  
   - При запуске игры программа приветствует игрока и объясняет правила:
     ```
     Добро пожаловать в игру HMRABI!
     Я загадаю число в диапазоне от 1 до 100.
     Ваша задача — угадать его.
     Я буду показывать, насколько близким является ваше предположение.
     У вас есть неограниченное количество попыток.
     ```

   - Программа генерирует случайное число в диапазоне от 1 до 100.

#### 2. **Основной процесс игры**
   - **Ввод игрока:**
     1. Игрок вводит своё предположение, пытаясь угадать число.
     2. Программа сравнивает введённое число с загаданным и сообщает, насколько оно близко к правильному:
        - "Холодно" — если введённое число далеко от загаданного.
        - "Тёпло" — если число близко, но ещё не угадано.
        - "Горячо" — если число очень близко.
        - "Поздравляю!" — если число угадано правильно.

   - **Количество попыток:**
     1. Игрок может вводить новые числа до тех пор, пока не угадает загаданное.

#### 3. **Завершение игры**
   - Когда игрок угадывает число, программа выводит поздравление:
     ```
     Поздравляю! Вы угадали число за X попыток!
     Хотите сыграть снова? (да/нет)
     ```

   - Если игрок выбирает "да", начинается новый раунд с новым загаданным числом.
   - Если "нет", программа завершает работу.

---

### Пример работы программы  

1. **Начало игры:**  
   ```  
   Добро пожаловать в игру HMRABI!  
   Я загадаю число от 1 до 100.  
   Ваша задача — угадать его.  
   У вас есть неограниченное количество попыток.  
   Введите ваше предположение:  
   > 50  
   Холодно!  
   Введите ваше предположение:  
   > 75  
   Тёпло!  
   Введите ваше предположение:  
   > 85  
   Горячо!  
   Введите ваше предположение:  
   > 87  
   Поздравляю! Вы угадали число за 4 попытки!  
   Хотите сыграть снова? (да/нет):  
   > нет  
   Спасибо за игру!  
   ```

---

### Возможные ограничения  
- Игрок может вводить только числовые значения в пределах от 1 до 100.  
- Программа должна адекватно реагировать на некорректный ввод (например, если введено не число или число вне диапазона).

---

### Реализация  
Игра может быть реализована на Python с использованием следующих возможностей:  
- **Модуль `random`** для генерации случайного числа в заданном диапазоне.  
- **Циклы и условия** для обработки ввода игрока, сравнения с загаданным числом и вывода подсказок.
- Логика для отображения подсказок ("холодно", "тёпло", "горячо").

Рекомендуется:  
- Реализовать добавление функционала для изменения диапазона чисел (например, от 1 до 1000) в зависимости от уровня сложности.
- Добавить возможность игры с таймером, чтобы подсчитывать, сколько времени игроку понадобилось для угадывания числа.