import pytest

from src.api_hh import HeadHunterAPI
from src.vacancy import Vacancy


@pytest.fixture
def test_vacancy_1():
    return {
        "id": "108374935",
        "name": "Python Developer/Разработчик Python",
        "salary": {
            "from": 1500,
            "to": None,
            "currency": "RUR",
        },
        "alternate_url": "https://hh.ru/vacancy/108374935",
        "snippet": {
            "requirement": "опыт работы с Docker.",
            "responsibility": "Поддержание системы. - Разработка нового функционала.",
        },
    }


@pytest.fixture
def test_vacancy_2():
    return {
        "id": "108374935",
        "name": "Python Developer/Разработчик Python",
        "salary": {
            "from": None,
            "to": 1800,
            "currency": "RUR",
        },
        "alternate_url": "https://hh.ru/vacancy/108374935",
        "snippet": {
            "requirement": "опыт работы с Docker.",
            "responsibility": "Поддержание системы. - Разработка нового функционала.",
        },
    }


@pytest.fixture
def test_vacancy_3():
    return {
        "id": "108374935",
        "name": "Python Developer/Разработчик Python",
        "salary": {
            "from": 1600,
            "to": 1800,
            "currency": "RUR",
        },
        "alternate_url": "https://hh.ru/vacancy/108374935",
        "snippet": {
            "requirement": "опыт работы с Docker.",
            "responsibility": "Поддержание системы. - Разработка нового функционала.",
        },
    }


@pytest.fixture
def vacancies_list(test_vacancy_1, test_vacancy_2, test_vacancy_3):
    return [test_vacancy_1, test_vacancy_2, test_vacancy_3]


@pytest.fixture
def test_vacancy_4():
    return {
        "id": "test4",
        "name": "test4",
        "salary": {
            "from": None,
            "to": 0,
            "currency": "RUR",
        },
        "alternate_url": "test4",
        "snippet": {"requirement": "test4", "responsibility": "test4"},
    }


@pytest.fixture
def test_vacancy_5():
    return {
        "id": "test4",
        "name": "test4",
        "salary": {
            "from": 4,
            "to": 0,
            "currency": "KZT",
        },
        "alternate_url": "test4",
        "snippet": {"requirement": "test4", "responsibility": "test4"},
    }


@pytest.fixture
def vac1():
    return {"id": "test1", "name": "test1", "salary": 1, "url": "test1", "description": "test1"}


@pytest.fixture
def vac2():
    return {"id": "test2", "name": "test2", "salary": "2", "url": "test2", "description": "test2"}


@pytest.fixture
def vac3():
    return {"id": "test2", "name": "test2", "salary": None, "url": "test2", "description": "test2"}


@pytest.fixture
def vac4():
    return {"id": "test2", "name": "test2", "url": "test2", "description": "test2"}


@pytest.fixture
def filter_words():
    return ["Django", "sql"]


@pytest.fixture
def vac_1():
    return Vacancy.new_vacancy({"id": 123, "name": "name", "description": "Python", "url": "test", "salary": 700})


@pytest.fixture
def vac_2():
    return Vacancy.new_vacancy({"id": 124, "name": "name", "description": "Django", "url": "test", "salary": 200})


@pytest.fixture
def vac_3():
    return Vacancy.new_vacancy({"id": 125, "name": "name", "description": "Django", "url": "test", "salary": 500})


@pytest.fixture
def vac_4():
    return Vacancy.new_vacancy({"id": 126, "name": "name", "description": "Docker", "url": "test", "salary": 1000})


@pytest.fixture
def vac_5():
    return Vacancy.new_vacancy({"id": 127, "name": "name", "description": "SQL", "url": "test", "salary": 100})


@pytest.fixture
def vac_6():
    return Vacancy.new_vacancy({"id": 128, "name": "name", "description": "SQL", "url": "test", "salary": 300})


@pytest.fixture
def vac_list(vac_1, vac_2, vac_3, vac_4, vac_5, vac_6):
    v_list = [vac_1, vac_2, vac_3, vac_4, vac_5, vac_6]
    return v_list


@pytest.fixture
def sorted_vac_list(vac_1, vac_2, vac_3, vac_4, vac_5, vac_6):
    return [vac_4, vac_1, vac_3, vac_6, vac_2, vac_5]


@pytest.fixture
def vac_list_salary(vac_6, vac_2):
    return [vac_2, vac_6]


@pytest.fixture
def vac_list_filter_words(vac_2, vac_3, vac_5, vac_6):
    return [vac_2, vac_3, vac_5, vac_6]
