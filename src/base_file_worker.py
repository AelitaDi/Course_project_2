from abc import ABC, abstractmethod


class FileWorker(ABC):
    """
    Абстрактный класс для работы с файлами.
    """

    @abstractmethod
    def file_reader(self):
        """
        Абстрактный метод для извлечения данных из файла.
        """
        pass

    @abstractmethod
    def file_writer(self, data):
        """
        Абстрактный метод для добавления данных в файл.
        """
        pass

    @abstractmethod
    def file_deleter(self):
        """
        Абстрактный метод для удаления данных из файла.
        """
        pass
