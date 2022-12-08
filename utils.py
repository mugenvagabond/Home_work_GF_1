# Импортируем библиотеку json и класс Question
import json


def get_file(filename):
    """
    Функция загрузки вопросов из json файла и создания списка
    :param filename: questions.json
    :return: questions
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_all():
    stroke = ""
    for item in get_file("candidates.json"):
        stroke += f"Имя кандидата - {item['name']}\n" \
                  f"Позиция кандидата - {item['position']}\n" \
                  f"Навыки - {item['skills']}\n\n"
    return stroke


def get_candidate_by_pk(pk):
    for item in get_file("candidates.json"):
        if pk == item["pk"]:
            stroke = f"<img src={item['picture']}>\n" \
                      f"Имя кандидата - {item['name']}\n" \
                      f"Позиция кандидата - {item['position']}\n" \
                      f"Навыки - {item['skills']}\n\n"
            return stroke


def get_by_skill(skill_name):
    stroke = ""
    for item in get_file("candidates.json"):
        skill_list = item['skills'].lower().split(', ')
        if skill_name.lower() in skill_list:
            stroke += f"Имя кандидата - {item['name']}\n" \
                     f"Позиция кандидата - {item['position']}\n" \
                     f"Навыки - {item['skills']}\n\n"
    return stroke

