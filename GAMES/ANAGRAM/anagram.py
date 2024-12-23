import google.generativeai as genai
import re

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, api_key: str, system_instruction: str = "", model_name: str = "gemini-2-13b"):
        """
        Инициализация модели GoogleGenerativeAI.
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction)

    def ask(self, q: str) -> str:
        """
        Отправляет текстовый запрос модели и возвращает ответ.
        """
        try:
            response = self.model.generate_content(q)
            return response.text
        except Exception as ex:
            return f"Error: {str(ex)}"

# Инструкция для Gemini
system_instruction = """
Ты — генератор анаграмм. Твоя задача — по заданному набору букв найти существующее слово русского языка, составленное из этих букв (используя все или часть из них).

Правила:

1.  Игнорируй любые символы, кроме русских букв. Цифры и другие символы не учитываются.
2.  Если из заданных букв можно составить несколько слов, верни одно из них.
3.  Если из заданных букв невозможно составить ни одного слова русского языка, верни ответ "Нет анаграмм".
4.  Не генерируй неологизмы или выдуманные слова. Используй только существующие слова русского языка.
5.  Не объясняй процесс, просто возвращай слово или "Нет анаграмм".
"""

API_KEY: str = input("API ключ от `gemini`: ")
model = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction)

if __name__ == "__main__":
    while True:
        q = input("Введите буквы, по которым Gemini подберет анаграмму: ")
        # Очистка ввода от не кириллических символов
        q = re.sub(r"[^а-яА-ЯёЁ]", "", q)
        if not q:
            print("Введены некорректные символы. Введите русские буквы.")
            continue
        response = model.ask(q)
        print(response)