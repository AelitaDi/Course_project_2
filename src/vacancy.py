from src.base_vacancy import BaseVacancy


class Vacancy(BaseVacancy):
    """
    Класс вакансий.
    """

    __slots__ = ("id", "name", "url", "description", "salary")

    def __init__(self, vac_id: str, name: str, url: str, description: str, salary: int):
        self.id = vac_id
        self.name = name
        self.url = url
        self.description = description
        self.salary = salary

    def __str__(self):
        return (
            f"Вакансия: \n {self.name}\n ЗП: {self.salary}\n Требования и обязанности: {self.description}"
            f"\n Ссылка:\n {self.url}"
        )

    @classmethod
    def new_vacancy(cls, new_vacancy_dict: dict):
        """
        Метод инициализации новой вакансии.
        """
        id_ = new_vacancy_dict.get("id")
        description = new_vacancy_dict.get("description")
        name = new_vacancy_dict.get("name")
        url = new_vacancy_dict.get("url")
        salary = Vacancy.__is_salary(new_vacancy_dict.get("salary", 0))
        return cls(id_, name, url, description, salary)

    def __le__(self, other) -> bool:
        """
        Метод реализует сравнение по зарплате меньше или равно.
        """
        return self.salary <= other.salary

    def __lt__(self, other) -> bool:
        """
        Метод реализует сравнение по зарплате меньше.
        """
        return self.salary < other.salary

    def __ge__(self, other) -> bool:
        """ \
        Метод реализует сравнение по зарплате больше или равно.
        """
        return self.salary >= other.salary

    def __gt__(self, other) -> bool:
        """
        Метод реализует сравнение по зарплате больше.
        """
        return self.salary > other.salary

    @staticmethod
    def __is_salary(salary: int | None | str) -> int:
        """
        Проверка данных о зарплате.
        """
        if salary is None or (type(salary) is str and not salary.isdigit()):
            return 0
        if type(salary) is str and salary.isdigit():
            return int(salary)
        else:
            return salary

    @property
    def vacancy_dict(self):
        """
        Метод возвращает словарь с атрибутами вакансии.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "url": self.url,
            "salary": self.salary,
        }
