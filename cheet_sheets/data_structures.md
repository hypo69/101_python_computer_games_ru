
**1. Списки (Lists)**

*   **Определение:** Списки в Python – это упорядоченные, изменяемые коллекции элементов. Это значит, что ты можешь добавлять, удалять и изменять элементы в списке, и порядок элементов имеет значение.
*   **Представление:** Списки создаются с помощью квадратных скобок `[]`, а элементы разделяются запятыми.
    ```python
    my_list = [1, 2, 3, "apple", "banana", True]
    ```
*   **Особенности:**
    *   Могут содержать элементы разных типов данных (числа, строки, булевы значения, другие списки и т.д.).
    *   Поддерживают индексацию (доступ к элементу по его позиции, начиная с 0).
    *   Изменяемые (mutable).

**2. Словари (Dictionaries)**

*   **Определение:** Словари в Python – это неупорядоченные коллекции элементов, где каждый элемент состоит из пары "ключ-значение".
*   **Представление:** Словари создаются с помощью фигурных скобок `{}`, а пары "ключ-значение" разделяются двоеточием `:`.
    ```python
    my_dict = {"name": "John", "age": 30, "city": "New York"}
    ```
*   **Особенности:**
    *   Ключи должны быть уникальными и неизменяемыми (обычно строки или числа), а значения могут быть любого типа.
    *   Доступ к значениям осуществляется по ключу.
    *   Изменяемые (mutable).
    *   Неупорядоченные (порядок может не сохранятся)

**3. Кортежи (Tuples)**

*   **Определение:** Кортежи в Python – это упорядоченные, **неизменяемые** коллекции элементов.
*   **Представление:** Кортежи создаются с помощью круглых скобок `()`, а элементы разделяются запятыми.
    ```python
    my_tuple = (1, 2, 3, "apple", "banana", True)
    ```
*   **Особенности:**
    *   Аналогичны спискам, но являются неизменяемыми (immutable), то есть нельзя изменить элементы после создания кортежа.
    *   Могут содержать элементы разных типов данных.
    *   Поддерживают индексацию.
    *   Используются для представления неизменяемых последовательностей.

**4. SimpleNamespace**

*   **Определение:** `SimpleNamespace` из модуля `types` - это простой класс, позволяющий создавать объекты, у которых атрибуты (свойства) можно задавать как при создании, так и потом.
*   **Представление:** Для создания объекта `SimpleNamespace` нужно импортировать его из `types` и передать в него именованные аргументы (или не передать их):
     ```python
    from types import SimpleNamespace
    
    my_namespace = SimpleNamespace(name="John", age=30, city="New York")
    ```
*  **Особенности:**
    *  Позволяет создавать объекты с динамическими атрибутами (похоже на словарь).
    *  Удобен для создания простых объектов для хранения данных.
    *  Атрибуты доступны через точку, как у обычных объектов: `my_namespace.name`
    *  В отличие от словарей, порядок атрибутов сохраняется.
    *  Поля можно менять, но нельзя добавлять новые поля

**5. Другие структуры данных в Python:**

*   **Множества (Sets):** (Мы их уже изучали)
    *   Неупорядоченные коллекции уникальных элементов.
    *   Представление: `{1, 2, 3, "apple"}`
    *   Изменяемые.
*   **Строки (Strings):**
    *   Последовательность символов.
    *   Представление: `"hello"`, `'world'`
    *   Неизменяемые (immutable).
    *   Поддерживают индексацию и многие другие операции.
*   **Байтовые массивы (Bytearrays):**
    *  Изменяемая последовательность байтов.
    *  Представление: `bytearray(b"hello")`
    *  Используются для работы с двоичными данными.
*   **Диапазоны (Ranges):**
    *   Последовательность целых чисел.
    *   Представление: `range(10)`, `range(1, 10, 2)`
    *   Неизменяемые.
    *   Используются для генерации последовательностей.
*   **Frozen sets (неизменяемые множества)**
    *   Неизменяемая версия множеств (sets).
    *  Представление `frozenset([1, 2, 3])`

**Примеры:**

```python
from types import SimpleNamespace

# Списки
my_list = [1, 2, 3, "apple", "banana"]
print(f"Список: {my_list}, элемент по индексу 1: {my_list[1]}")

# Словари
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(f"Словарь: {my_dict}, значение по ключу 'name': {my_dict['name']}")

# Кортежи
my_tuple = (1, 2, 3, "apple", "banana")
print(f"Кортеж: {my_tuple}, элемент по индексу 2: {my_tuple[2]}")

# SimpleNamespace
my_namespace = SimpleNamespace(name="John", age=30, city="New York")
print(f"SimpleNamespace: {my_namespace}, значение атрибута 'name': {my_namespace.name}")

# Множества
my_set = {1, 2, 3, "apple"}
print(f"Множество: {my_set}")
```

**Ключевые отличия:**

*   **Изменяемость (Mutability):**
    *   Списки, словари, множества и `SimpleNamespace` - изменяемые.
    *   Кортежи и строки - неизменяемые.
*   **Упорядоченность (Order):**
    *   Списки и кортежи – упорядоченные.
    *   Словари и множества – неупорядоченные (порядок не гарантируется, но `SimpleNamespace` сохраняет порядок)
*   **Ключи/Значения:**
    *   Словари используют пары ключ-значение.
    *   Остальные структуры хранят только значения.