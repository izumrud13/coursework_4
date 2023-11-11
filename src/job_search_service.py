from abc import ABC, abstractmethod


class API(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def add_profession(self, value):
        pass

    @abstractmethod
    def formated_data(self, data):
        pass


class Saver(ABC):

    @abstractmethod
    def __init__(self, path):
        pass

    @abstractmethod
    def file_saving(self, data):
        pass