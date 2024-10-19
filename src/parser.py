from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Абстрактный класс для работы с API.
    """

    @abstractmethod
    def __get_response(self):
        """
        Абстрактный метод для подключения к API
        """
        pass

    @abstractmethod
    def get_vacancies(self, keyword):
        pass
