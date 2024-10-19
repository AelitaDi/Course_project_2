from src.api_hh import HeadHunterAPI
from src.utils import (filter_vacancies, get_top_vacancies, get_vacancies_by_salary, get_vacancy_list, print_vacancies,
                       sort_vacancies)


def user_interaction():
    # platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат (Пример: 100000 - 150000): ")

    list_vacancies_hh = HeadHunterAPI().get_vacancies(search_query)

    vacancies_list = get_vacancy_list(list_vacancies_hh)

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    if len(top_vacancies) == 0:
        print("По вашим параметрам не найдено ни одной вакансии.")
    else:
        print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
