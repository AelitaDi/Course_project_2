from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, get_vacancy_list
from src.vacancy import Vacancy


def test_get_vacancy_list(vacancy_list):
    v1 = Vacancy.new_vacancy({'id': 1, 'name': 'test1', 'url': 'test1', 'description': 'test1', 'salary': 100})
    v2 = Vacancy.new_vacancy({'id': 2, 'name': 'test2', 'url': 'test2', 'description': 'test2', 'salary': 200})
    v3 = Vacancy.new_vacancy({'id': 3, 'name': 'test3', 'url': 'test3', 'description': 'tEst3', 'salary': 300})
    v4 = Vacancy.new_vacancy({'id': 4, 'name': 'test4', 'url': 'test4', 'description': 'test4', 'salary': 400})
    assert get_vacancy_list(vacancy_list) == [v1, v2, v3, v4]


def test_filter_vacancies(vacancy_list, filter_words):
    assert filter_vacancies(vacancy_list, filter_words) == [{
            'id': 2,
            'name': 'test2',
            'url': 'test2',
            'description': 'test2',
            'salary': 200
        },
        {
            'id': 3,
            'name': 'test3',
            'url': 'test3',
            'description': 'tEst3',
            'salary': 300
        }]


def test_get_vacancies_by_salary(vacancy_list):
    assert get_vacancies_by_salary(vacancy_list, '200 - 300') == [{
            'id': 2,
            'name': 'test2',
            'url': 'test2',
            'description': 'test2',
            'salary': 200
        },
        {
            'id': 3,
            'name': 'test3',
            'url': 'test3',
            'description': 'tEst3',
            'salary': 300
        }]


def test_sort_vacancies(vac_list, sorted_vac_list):
    assert sort_vacancies(vac_list) == sorted_vac_list


def test_get_top_vacancies(sorted_vac_list, vac_4, vac_1, vac_3):
    assert get_top_vacancies(sorted_vac_list, 3) == [vac_4, vac_1, vac_3]
