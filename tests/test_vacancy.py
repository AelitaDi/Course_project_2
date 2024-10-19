from src.vacancy import Vacancy


def test_print_vacancy(vac_1, vac_2, capsys):
    print(vac_1)
    message = capsys.readouterr()
    assert message.out == f'Вакансия: \n name\n ЗП: 700\n Требования и обязанности: Python\n Ссылка:\n test\n'
    print(vac_2)
    message = capsys.readouterr()
    assert message.out == f'Вакансия: \n name\n ЗП: 200\n Требования и обязанности: Django\n Ссылка:\n test\n'


def test__vac_vs_vac__(vac_1, vac_2):
    assert (vac_2 <= vac_1) is True
    assert (vac_1 < vac_2) is False
    assert (vac_1 > vac_2) is True
    assert (vac_2 >= vac_1) is False


def test_new_vacancy(vac1, vac2, vac3, vac4):
    vacancy_1 = Vacancy.new_vacancy(vac1)
    assert vacancy_1.salary == 1
    assert vacancy_1.id == "test1"
    assert vacancy_1.name == "test1"
    assert vacancy_1.description == "test1"
    assert vacancy_1.url == "test1"
    vacancy_2 = Vacancy.new_vacancy(vac2)
    assert vacancy_2.salary == 2
    assert vacancy_2.id == "test2"
    assert vacancy_2.name == "test2"
    assert vacancy_2.description == "test2"
    assert vacancy_2.url == "test2"
    vacancy_3 = Vacancy.new_vacancy(vac3)
    assert vacancy_3.salary == 0
    vacancy_4 = Vacancy.new_vacancy(vac4)
    assert vacancy_4.salary == 0


def test_vacancy_dict(vac1):
    vacancy_1 = Vacancy.new_vacancy(vac1)
    assert vacancy_1.vacancy_dict == {
        "id": "test1",
        "name": "test1",
        "description": "test1",
        "url": "test1",
        "salary": 1,
    }
