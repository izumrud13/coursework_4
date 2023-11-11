import copy
import requests

from src.job_search_service import API
from src.vacancies import Vacancies


class SuperJobAPI(API):
    """
    Obtaining information from the API of the superjob.ru website
    """
    __SJ_API_URL = 'https://api.superjob.ru/2.0/vacancies/'
    __SJ_API_KEY = 'v3.r.137939262.2cdae9780058f951ba6d7ca739757cabfee656af.7222c5992af77f3e8f94ce21882bbd3026de8c8f'
    param_default = {
        'count': 50,
        'town': 'Москва',
        'period': 7,
    }

    def __init__(self):
        self.param = copy.deepcopy(self.param_default)

    def get_vacancies(self):
        """
        Receiving information via API about vacancies
        """

        headers = {'X-Api-App-Id': self.__SJ_API_KEY}

        response = requests.get(self.__SJ_API_URL, headers=headers, params=self.param)
        if response.status_code == 200:
            return response.json()['objects']
        else:
            return None

    def add_profession(self, value: str) -> None:
        """
        Adding the 'keyword' parameter to param
        :param value: string
        """
        self.param['keyword'] = value
        Vacancies.request_text = value

    def formated_data(self, data: list) -> list:
        """
        Data formatting
        :param data: list
        :return: list
        """

        work_data = []
        for item in data:
            if item['payment_to'] == 0:
                salary = item['payment_from']
            else:
                salary = item['payment_to']
            requirement = item['candidat']
            requirement = requirement.replace('\n', ' ')
            work_dict = {'name': item['profession'],
                         'requirement': requirement,
                         'responsibility': item['catalogues'][0]['title'],
                         'salary': salary,
                         'salary_currency': 'руб',
                         'url': item['link'],
                         'employer': item['firm_name']
                         }
            work_data.append(work_dict)
        return work_data
