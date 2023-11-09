from abc import ABC, abstractmethod


class JobSearchService(ABC):

    @abstractmethod
    def get_vacancies(self, search):
        pass

