import json
from datetime import datetime
from functions import load_data_from_json, get_user_level, base_program, get_result

def main():
    # имя
    username = input("Введите ваше имя: ").strip()

    # данные
    json_file = "questions.json"
    data = load_data_from_json(json_file)
    levels = data[1]["levels"]


    user_lvl = input("Выберите уровень сложности \nлегкий, средний, сложный.\n").lower()
    test_words = get_user_level(user_lvl, data)
    test_answers = base_program(test_words)
    result = get_result(test_answers, levels)


    result_file = f"results_{username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(result_file, "w", encoding="utf-8") as file:
        json.dump({"username": username, "answers": test_answers, "rank": result}, file, ensure_ascii=False, indent=4)

    print(f"Ваш результат сохранен в файл {result_file}")

if __name__ == "__main__":
    main()