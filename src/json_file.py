import json

from src.job_search_service import Saver


class InfoSaver(Saver):
    """
    Class for saving information to json file
    """

    def __init__(self, path='D:\Pyyhon\coursework_4\src\data.json'):
        self.path = path

    def file_saving(self, data: list):
        """
        Saving data to a file
        :param data: list
        """
        with open(self.path, 'w', encoding='windows-1251') as file:
            file.write(json.dumps(data, indent=2, ensure_ascii=False))
