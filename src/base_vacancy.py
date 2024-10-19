from abc import ABC, abstractmethod


class BaseVacancy(ABC):
    """
    Абстрактный класс для вакансий.
    """

    @classmethod
    @abstractmethod
    def new_vacancy(cls, *args, **kwargs):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def __le__(self, other):
        pass

    @abstractmethod
    def __gt__(self, other):
        pass

    @abstractmethod
    def __ge__(self, other):
        pass
