import requests

from src.parser import Parser


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter.
    """

    def __init__(self):
        """
        Создание экземпляра класса, атрибутов для подключения к API HH.
        """
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        # super().__init__(file_worker)

    @property
    def url(self):
        return self.__url

    @property
    def headers(self):
        return self.__headers

    @property
    def params(self):
        return self.__params

    def _Parser__get_response(self) -> bool:
        """
        Метод получения ответа от HH, проверка статуса ответа.
        """
        self.__params["page"] = 0
        response = requests.get("https://api.hh.ru/", headers=self.__headers, params=self.__params)
        self.__status_code = response.status_code
        if self.__status_code == 200:
            print("Ответ от HH.ru успешно получен.")
            return True
        else:
            print(f"Ошибка подключения к HH.ru. Status code: {self.__status_code}")
            return False

    def get_vacancies(self, keyword: str, per_page: int = 100) -> list[dict]:
        """
        Метод Загружает вакансии по ключевому слову.
        """
        vacancies = []
        if self._Parser__get_response():
            self.__params["text"] = keyword
            self.__params["per_page"] = per_page
            while requests.get(self.__url, headers=self.__headers, params=self.__params):
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                vacancies.extend(response.json()["items"])
                self.__params["page"] += 1
        return vacancies

    @staticmethod
    def get_price(currency: str) -> float:
        """
        Метод получает курс валюты.
        """
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        courses = response.json()
        if courses["Valute"].get(currency):
            price = courses["Valute"][currency].get("Value")
        else:
            price = 1
        return price

    @classmethod
    def transfom_data(cls, vacancy: dict) -> dict:
        """
        Метод преобразовывает вакансии в формат, с которым удобно работать.
        """
        salary = 0
        if type(vacancy.get("salary")) == dict:
            from_ = vacancy["salary"].get("from", 0)
            to = vacancy["salary"].get("to", 0)
            if (from_ is not None and from_ != 0) and (to is not None and to != 0):
                salary = (from_ + to) // 2
            elif from_ is not None and from_ != 0:
                salary = from_
            elif to is not None and to != 0:
                salary = to

            if salary != 0 and vacancy["salary"]["currency"] != "RUR":
                salary = salary * cls.get_price(vacancy["salary"]["currency"])

        transformed_vacancy = {
            "id": vacancy["id"],
            "name": vacancy["name"],
            "salary": salary,
            "url": vacancy.get("alternate_url", ""),
            "description": f"Обязанности: {vacancy['snippet'].get('responsibility', '')} "
            f"Требования: {vacancy['snippet'].get('requirement', '')}",
        }
        return transformed_vacancy


if __name__ == "__main__":
    HeadHunterAPI().get_vacancies()
#     # print(HeadHunterAPI.get_price("BYR"))
#     print(HeadHunterAPI.transfom_data({
#         'id': '108374935',
#         'name': 'Python Developer/Разработчик Python',
#         'salary': {
#             'from': 1600,
#             'to': 1800,
#             'currency': 'RUR',
#         },
#         'alternate_url': 'https://hh.ru/vacancy/108374935',
#         'snippet': {
#             'requirement': 'опыт работы с Docker.',
#             'responsibility': 'Поддержание системы. - Разработка нового функционала'
#         }
#     }))
