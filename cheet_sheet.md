Азы программирования для языка **Python** включают основы, которые помогут быстро освоить этот язык и начать создавать программы. Python считается одним из самых простых языков для начинающих благодаря читаемому синтаксису и огромному количеству библиотек.

---

### **1. Переменные и типы данных**
- Переменные: создание и использование.  
  ```python
  name = 'Alice'  # Переменная типа строка
  age = 25        # Переменная типа число
  ```
- Основные типы данных:
  - `int` (целое число): `x = 10`
  - `float` (вещественное число): `y = 3.14`
  - `str` (строка): `name = 'Python'`
  - `bool` (логический): `is_active = True`
  - `list` (список): `numbers = [1, 2, 3]`
  - `dict` (словарь): `user = {'name': 'Alice', 'age': 25}`
  - `tuple` (кортеж): `coordinates = (10, 20)`
  - `set` (множество): `unique_numbers = {1, 2, 3}`

---

### **2. Ввод и вывод данных**
- **Ввод данных** от пользователя:
  ```python
  name = input('Введите ваше имя: ')
  print(f'Привет, {name}!')
  ```
- **Вывод данных** на экран:
  ```python
  print('Hello, Python!')
  ```

---

### **3. Условные конструкции**
- Использование `if-else` для принятия решений:
  ```python
  age = int(input('Введите ваш возраст: '))
  if age >= 18:
      print('Вы совершеннолетний.')
  else:
      print('Вы несовершеннолетний.')
  ```
- Оператор `elif` для проверки нескольких условий:
  ```python
  score = 85
  if score >= 90:
      print('Отлично!')
  elif score >= 75:
      print('Хорошо!')
  else:
      print('Старайтесь лучше.')
  ```

---

### **4. Циклы**
- Цикл `for` для работы с последовательностями:
  ```python
  for i in range(5):
      print(f'Итерация {i}')
  ```
- Цикл `while` для выполнения кода, пока условие истинно:
  ```python
  n = 0
  while n < 5:
      print(n)
      n += 1
  ```

---

### **5. Функции**
- Создание функций:
  ```python
  def greet(name):
      print(f'Привет, {name}!')
  
  greet('Python')
  ```
- Функции с возвращаемыми значениями:
  ```python
  def add(a, b):
      return a + b
  
  result = add(5, 3)
  print(result)  # 8
  ```

---

### **6. Работа со списками**
- Основные операции со списками:
  ```python
  numbers = [1, 2, 3, 4]
  numbers.append(5)       # Добавление элемента
  numbers.remove(3)       # Удаление элемента
  numbers[0] = 10         # Изменение элемента
  print(numbers)          # [10, 2, 4, 5]
  ```

- Перебор элементов списка:
  ```python
  for number in numbers:
      print(number)
  ```

---

### **7. Словари**
- Создание и работа со словарями:
  ```python
  user = {'name': 'Alice', 'age': 25}
  print(user['name'])     # Alice
  user['age'] = 26        # Изменение значения
  user['city'] = 'NYC'    # Добавление ключа
  print(user)             # {'name': 'Alice', 'age': 26, 'city': 'NYC'}
  ```

- Перебор ключей и значений:
  ```python
  for key, value in user.items():
      print(f'{key}: {value}')
  ```

---

### **8. Обработка ошибок**
- Использование `try-except`:
  ```python
  try:
      number = int(input('Введите число: '))
      print(f'Квадрат числа: {number ** 2}')
  except ValueError as ex:
      print('Это не число!', ex)
  ```

---

### **9. Работа с файлами**
- Чтение и запись в файлы:
  ```python
  # Запись
  with open('example.txt', 'w') as file:
      file.write('Hello, Python!')

  # Чтение
  with open('example.txt', 'r') as file:
      content = file.read()
      print(content)
  ```

---

### **10. Модули и библиотеки**
- Импорт и использование модулей:
  ```python
  import math
  print(math.sqrt(16))  # 4.0
  ```

- Установка и использование библиотек:
  ```bash
  pip install requests
  ```
  ```python
  import requests
  response = requests.get('https://api.github.com')
  print(response.json())
  ```

---

1. Практикуйтся ежедневно: решай простые задачи на Python.
2. Изучай документацию Python: [https://docs.python.org/](https://docs.python.org/).
3. Создавай небольшие проекты: например, калькулятор или список дел.