from src.vacancy import Vacancy


def test__vac_vs_vac__(vac1, vac2):
    vacancy1 = Vacancy.new_vacancy(vac1)
    vacancy2 = Vacancy.new_vacancy(vac2)
    assert (vacancy1 <= vacancy2) is True
    assert (vacancy2 < vacancy1) is False
    assert (vacancy2 > vacancy1) is True
    assert (vacancy1 >= vacancy2) is False


def test_new_vacancy(vac1, vac2, vac3, vac4):
    vacancy_1 = Vacancy.new_vacancy(vac1)
    assert vacancy_1.salary == 1
    assert vacancy_1.id == 'test1'
    assert vacancy_1.name == 'test1'
    assert vacancy_1.description == 'test1'
    assert vacancy_1.url == 'test1'
    vacancy_2 = Vacancy.new_vacancy(vac2)
    assert vacancy_2.salary == 2
    assert vacancy_2.id == 'test2'
    assert vacancy_2.name == 'test2'
    assert vacancy_2.description == 'test2'
    assert vacancy_2.url == 'test2'
    vacancy_3 = Vacancy.new_vacancy(vac3)
    assert vacancy_3.salary == 0
    vacancy_4 = Vacancy.new_vacancy(vac4)
    assert vacancy_4.salary == 0


def test_vacancy_dict(vac1):
    vacancy_1 = Vacancy.new_vacancy(vac1)
    assert vacancy_1.vacancy_dict == {'id': 'test1', 'name': 'test1', 'description': 'test1', 'url': 'test1',
                                      'salary': 1}
