from src.api_hh import HeadHunterAPI
from src.vacancy import Vacancy


def get_vacancy_list(vacancies_list_dict: list[dict]) -> list[Vacancy]:
    """
    Получает список экземпляров класса Vacancy из списка словарей.
    """
    target_list = list(map(lambda x: Vacancy.new_vacancy(HeadHunterAPI.transfom_data(x)), vacancies_list_dict))
    return target_list


def filter_vacancies(vacancies_list: list[Vacancy], filter_words: list[str]) -> list[Vacancy]:
    """
    Функция для фильтрации вакансий по ключевым словам.
    """
    target_list = []
    for vacancy in vacancies_list:
        for word in filter_words:
            if word.lower() in vacancy.vacancy_dict['description'].lower():
                target_list.append(vacancy)
                continue
    return target_list


def get_vacancies_by_salary(vacancies_list: list[Vacancy], salary_range: str) -> list[Vacancy]:
    """
    Функция фильтрует вакансии по зарплате.
    """
    target_list = []
    s_range = list(map(lambda x: int(x), salary_range.split(' - ')))
    range_min = s_range[0]
    range_max = s_range[-1]
    for vac in vacancies_list:
        if (vac.vacancy_dict['salary'] >= range_min) and (vac.vacancy_dict['salary'] <= range_max):
            target_list.append(vac)
    return target_list


def sort_vacancies(vac_list: list[Vacancy]) -> list[Vacancy]:
    """
    Функция сортировки списка вакансий по зарплате.
    """
    target_list = sorted(vac_list, key=lambda x: x.vacancy_dict['salary'], reverse=True)
    return target_list


def get_top_vacancies(vac_list: list[Vacancy], top_n: int) -> list[Vacancy]:
    """
    Функция обрезает список вакансий до N.
    """
    return vac_list[0: (top_n if top_n <= len(vac_list) else len(vac_list))]


def print_vacancies(vac_list: list[Vacancy]):
    """
    Функция выводит в консоль список вакансий.
    """
    for vacancy in vac_list:
        print(vacancy)


if __name__ == "__main__":
    vac1 = Vacancy.new_vacancy({"id": 123, "name": 'name', "description": "test", "url": "test", "salary": 7})
    vac2 = Vacancy.new_vacancy({"id": 124, "name": 'name', "description": "test", "url": "test", "salary": 2})
    vac3 = Vacancy.new_vacancy({"id": 125, "name": 'name', "description": "test", "url": "test", "salary": 5})
    vac4 = Vacancy.new_vacancy({"id": 126, "name": 'name', "description": "test", "url": "test", "salary": 10})
    vac5 = Vacancy.new_vacancy({"id": 127, "name": 'name', "description": "test", "url": "test", "salary": 1})
    vac6 = Vacancy.new_vacancy({"id": 128, "name": 'name', "description": "test", "url": "test", "salary": 3})
    v_list = [vac1, vac2, vac3, vac4, vac5, vac6]
    sort_list = sort_vacancies(v_list)
    top_n_list = get_top_vacancies(sort_list, 4)
    print_vacancies(top_n_list)
