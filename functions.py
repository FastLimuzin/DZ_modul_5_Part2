import json
import random

def load_data_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def get_user_level(level_choice, data):
    levels = {
        "легкий": 0,
        "средний": 1,
        "тяжелый": 2,
        "easy": 0,
        "medium": 1,
        "hard": 2
    }
    return data[0]["questions"][levels.get(level_choice, 0)]

def base_program(words):
    answers = {}
    print("\nНачнем игру! Переведите следующие слова:")
    for word, translation in random.sample(list(words.items()), len(words)):
        hint = f"{len(translation)} букв, начинается на '{translation[0]}'"
        print(f"Слово: {word} ({hint})")

        user_answer = input("Ваш перевод: ").strip().lower()
        if user_answer == translation.lower():
            print(f"Верно! {word.capitalize()} — это {translation}.")
            answers[word] = True
        else:
            print(f"Неверно. {word.capitalize()} — это {translation}.")
            answers[word] = False
    return answers

def get_result(answers, levels):
    correct_words = [word for word, correct in answers.items() if correct]
    incorrect_words = [word for word, correct in answers.items() if not correct]

    print("\nРезультаты:")
    print("Правильно отвечены слова:", ", ".join(correct_words) if correct_words else "нет")
    print("Неправильно отвечены слова:", ", ".join(incorrect_words) if incorrect_words else "нет")

    score = len(correct_words)
    rank = levels.get(str(score), "Неизвестный ранг")
    print(f"\nВаш ранг: {rank}")
    return rank