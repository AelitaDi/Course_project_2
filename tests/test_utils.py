from src.api_hh import HeadHunterAPI
from src.utils import filter_vacancies, get_top_vacancies, get_vacancies_by_salary, get_vacancy_list, sort_vacancies
from src.vacancy import Vacancy


def test_get_vacancy_list(vacancies_list, test_vacancy_1, test_vacancy_2, test_vacancy_3):
    v1 = Vacancy.new_vacancy(HeadHunterAPI.transfom_data(test_vacancy_1))
    v2 = Vacancy.new_vacancy(HeadHunterAPI.transfom_data(test_vacancy_2))
    v3 = Vacancy.new_vacancy(HeadHunterAPI.transfom_data(test_vacancy_3))
    test_list = get_vacancy_list(vacancies_list)
    assert test_list[0].vacancy_dict == v1.vacancy_dict
    assert test_list[1].vacancy_dict == v2.vacancy_dict
    assert test_list[2].vacancy_dict == v3.vacancy_dict


def test_filter_vacancies(vac_list_filter_words, filter_words, vac_list):
    assert filter_vacancies(vac_list, filter_words) == vac_list_filter_words


def test_get_vacancies_by_salary(vac_list, vac_list_salary):
    assert get_vacancies_by_salary(vac_list, "200 - 300") == vac_list_salary


def test_sort_vacancies(vac_list, sorted_vac_list):
    assert sort_vacancies(vac_list) == sorted_vac_list


def test_get_top_vacancies(sorted_vac_list, vac_4, vac_1, vac_3):
    assert get_top_vacancies(sorted_vac_list, 3) == [vac_4, vac_1, vac_3]
