
WEKDAY:
=================
Сложность: 4
-----------------
Игра "Какой день недели?" - это игра, в которой компьютер просит пользователя ввести номер дня года (от 1 до 366), а затем сообщает, какой это день недели. Игра учитывает високосные годы.

Правила игры:
1. Пользователю предлагается ввести номер дня в году (от 1 до 366).
2. Компьютер определяет, является ли год високосным.
3. Компьютер вычисляет день недели, соответствующий введенному номеру дня.
4. Компьютер выводит день недели.
-----------------
Алгоритм:
1. Вывести приглашение пользователю ввести день года.
2. Получить ввод пользователя и преобразовать его в целое число.
3. Вывести приглашение пользователю ввести год.
4. Получить ввод пользователя и преобразовать его в целое число.
5. Вычислить, является ли год високосным.
6. Вычислить день недели, используя остаток от деления количества дней на 7. (1 - воскресенье, 2- понедельник, ..., 7- суббота)
7. Вывести день недели.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InputDay["Ввод номера дня в году: <code><b>dayOfYear</b></code>"]
    InputDay --> InputYear["Ввод года: <code><b>year</b></code>"]
    InputYear --> IsLeapYear{"Проверка: <code><b>год високосный?</b></code>"}
    IsLeapYear -- Да --> CalculateDayOfWeekLeap["Вычисление дня недели для високосного года"]
    IsLeapYear -- Нет --> CalculateDayOfWeekNonLeap["Вычисление дня недели для обычного года"]
    CalculateDayOfWeekLeap --> OutputDayOfWeek["Вывод дня недели"]
    CalculateDayOfWeekNonLeap --> OutputDayOfWeek
    OutputDayOfWeek --> End["Конец"]

```
**Legenda**:
    Start - Начало программы.
    InputDay - Запрос у пользователя номера дня в году и сохранение в переменной dayOfYear.
    InputYear - Запрос у пользователя года и сохранение в переменной year.
    IsLeapYear - Проверка, является ли введенный год високосным.
    CalculateDayOfWeekLeap - Вычисление дня недели для високосного года.
    CalculateDayOfWeekNonLeap - Вычисление дня недели для обычного года.
    OutputDayOfWeek - Вывод дня недели на экран.
    End - Конец программы.
"""
__author__ = 'hypo69 (hypo69@davidka.net)'

# Запрашиваем у пользователя номер дня в году
try:
    dayOfYear = int(input("Введите номер дня в году (1-366): "))
    if not 1 <= dayOfYear <= 366:
         print("Пожалуйста, введите число от 1 до 366.")
         exit()
except ValueError:
    print("Пожалуйста, введите целое число.")
    exit()


# Запрашиваем у пользователя год
try:
    year = int(input("Введите год: "))
except ValueError:
    print("Пожалуйста, введите целое число.")
    exit()


# Определяем, является ли год високосным
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Вычисляем день недели 
if isLeapYear:
    dayOfWeek = (dayOfYear + 2) % 7 # 1 января високосного года - понедельник (второй день недели), поэтому добавляем 2
else:
    dayOfWeek = (dayOfYear + 1) % 7 # 1 января обычного года - воскресенье (первый день недели), поэтому добавляем 1

# Сопоставляем число дня недели со строковым представлением
days = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
dayOfWeekStr = days[dayOfWeek] if dayOfWeek > 0 else days[6]  # Если 0, то это суббота


# Выводим результат
print(f"Это {dayOfWeekStr}.")

"""
Объяснение кода:
1.  **Ввод данных**:
    -   `try...except ValueError`: Блоки `try...except` используются для обработки возможных ошибок при вводе данных пользователем. Если пользователь вводит что-то, что нельзя преобразовать в целое число, программа выведет сообщение об ошибке и завершится.
    -   `dayOfYear = int(input("Введите номер дня в году (1-366): "))`: Запрашивает у пользователя ввод номера дня в году и преобразует ввод в целое число.
    -    `if not 1 <= dayOfYear <= 366`: Проверяет, является ли введенное число допустимым днем в году (1-366). Если нет, выводит сообщение об ошибке и завершает программу.
    -   `year = int(input("Введите год: "))`: Запрашивает у пользователя ввод года и преобразует ввод в целое число.
2.  **Определение високосного года**:
    -   `isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)`: Определяет, является ли введенный год високосным. Год является високосным, если он делится на 4, но не делится на 100, или если он делится на 400.
3.  **Вычисление дня недели**:
    -   `if isLeapYear:`: Проверяет, является ли год високосным.
        - `dayOfWeek = (dayOfYear + 2) % 7`: Если год високосный, добавляем 2 к номеру дня, так как 1 января високосного года - понедельник. Вычисляем остаток от деления на 7, что дает нам день недели (0 - воскресенье, 1 - понедельник, ..., 6 - суббота).
    -   `else:`: Если год не високосный.
        -   `dayOfWeek = (dayOfYear + 1) % 7`:  Если год не високосный, добавляем 1 к номеру дня, так как 1 января обычного года - воскресенье. Также вычисляем остаток от деления на 7.
4.  **Преобразование числа дня недели в строку**:
     -   `days = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]`: Список названий дней недели.
     - `dayOfWeekStr = days[dayOfWeek] if dayOfWeek > 0 else days[6]`: Преобразуем число дня недели в строку, используя список `days`.  Если `dayOfWeek` равен 0, устанавливаем день недели как "Суббота".
5.  **Вывод результата**:
    -   `print(f"Это {dayOfWeekStr}.")`: Выводит сообщение с днем недели на экран.
"""
```