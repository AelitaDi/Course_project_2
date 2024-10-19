from unittest.mock import patch

import pytest

from src.api_hh import HeadHunterAPI


@patch("requests.get")
def test_get_price(mock_get):
    mock_get.return_value.json.return_value = {"Valute": {"TEST": {"Value": 23}}}
    assert HeadHunterAPI.get_price("TEST") == 23
    assert HeadHunterAPI.get_price("TEST_1") == 1


def test_headhunter_api():
    test = HeadHunterAPI()
    assert test.url == "https://api.hh.ru/vacancies"
    assert test.headers == {"User-Agent": "HH-User-Agent"}
    assert test.params == {"text": "", "page": 0, "per_page": 100}


def test_transform_data(test_vacancy_1, test_vacancy_2, test_vacancy_3, test_vacancy_4):
    assert HeadHunterAPI.transfom_data(test_vacancy_1) == {
        "id": "108374935",
        "name": "Python Developer/Разработчик Python",
        "salary": 1500,
        "url": "https://hh.ru/vacancy/108374935",
        "description": "Обязанности: Поддержание системы. - Разработка нового функционала. Требования: опыт работы с Docker.",
    }
    assert HeadHunterAPI.transfom_data(test_vacancy_2) == {
        "id": "108374935",
        "name": "Python Developer/Разработчик Python",
        "salary": 1800,
        "url": "https://hh.ru/vacancy/108374935",
        "description": "Обязанности: Поддержание системы. - Разработка нового функционала. Требования: опыт работы с Docker.",
    }
    assert HeadHunterAPI.transfom_data(test_vacancy_3) == {
        "id": "108374935",
        "name": "Python Developer/Разработчик Python",
        "salary": 1700,
        "url": "https://hh.ru/vacancy/108374935",
        "description": "Обязанности: Поддержание системы. - Разработка нового функционала. Требования: опыт работы с Docker.",
    }
    assert HeadHunterAPI.transfom_data(test_vacancy_4) == {
        "id": "test4",
        "name": "test4",
        "salary": 0,
        "url": "test4",
        "description": "Обязанности: test4 Требования: test4",
    }


@patch("src.api_hh.HeadHunterAPI.get_price")
def test_transform_data_with_get_price(mock_get_price, test_vacancy_5):
    mock_get_price.return_value = 2
    assert HeadHunterAPI.transfom_data(test_vacancy_5) == {
        "id": "test4",
        "name": "test4",
        "salary": 8,
        "url": "test4",
        "description": "Обязанности: test4 Требования: test4",
    }
