import json
import os

from src.base_file_worker import FileWorker
from src.vacancy import Vacancy


class JSONFileWorker(FileWorker):
    """
    Класс для работы с JSON-файлами.
    """

    def __init__(self,
                 filename: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "vacancies.json")):
        """
        Конструктор класса.
        """
        self.__filename = filename
        try:
            with open(self.__filename, encoding="utf-8") as file:
                data = json.load(file)
                self.exist = True
        except Exception:
            print('Файл не существует')
            self.exist = False

    # def exist_file(self) -> bool:
    #     """
    #     Метод проверяет существование файла.
    #     """
    #     flag = False
    #     try:
    #         self.file_reader()
    #         flag = True
    #     except Exception:
    #         print(f'Файл не существует')
    #     finally:
    #         return flag

    @staticmethod
    def exist_vacancy(target_vac: Vacancy, vac_list: list[Vacancy]):
        """
        Метод проверяет наличие вакансии в списке
        """
        for vac in vac_list:
            if vac.vacancy_dict.get('id') == target_vac.vacancy_dict.get('id'):
                # print(f'Вакансия {vac.get('id')} уже существует')
                return True
        return False

    @property
    def file_reader(self):
        """
        Метод для извлечения данных из JSON-файла.
        """
        if self.exist:
            with open(self.__filename, encoding="utf-8") as file:
                data = json.load(file)
            return data
        else:
            return []

    def file_writer(self, vacancy: Vacancy):
        """
        Метод для добавления данных в JSON-файл.
        """
        vacancy_dict = vacancy.vacancy_dict
        if not self.exist:
            print(f'Создаю новый файл {self.__filename}')
            with open(self.__filename, "w") as file:
                self.exist = True
                add_data = [vacancy_dict]
                json.dump(add_data, file)

        else:
            data = self.file_reader()
            if not JSONFileWorker.exist_vacancy(vacancy, data):
                with open(self.__filename, "w") as file:
                    data.append(vacancy_dict)
                    json.dump(data, file)

    def file_deleter(self):
        """
        Метод для удаления данных из JSON-файла.
        """
        with open(self.__filename, "w") as file:
            json.dump([], file)
            self.exist = True
            print(f'Файл {self.__filename} очищен.')


if __name__ == '__main__':
    vac_1 = Vacancy.new_vacancy({"id": 124, "name": 'test', "description": "test", "url": "test", "salary": 1})
    print(JSONFileWorker().file_reader)
    # JSONFileWorker().file_writer(vac_1)
    # JSONFileWorker().file_deleter()
