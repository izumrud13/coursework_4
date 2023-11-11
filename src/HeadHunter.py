import copy

import requests

from src.job_search_service import API
from src.vacancies import Vacancies


class HeadHunterAPI(API):
    """
    Obtaining information from the API of the headhunter.ru website
    """

    __HH_API_URL = 'https://api.hh.ru/vacancies'

    param_default = {
        'per_page': 50,
        'area': 1,
        'date': 7,
        'only_with_salary': True
    }

    def __init__(self):
        self.param = copy.deepcopy(self.param_default)

    def get_vacancies(self):
        """
        Receiving information via API about vacancies
        """
        response = requests.get(self.__HH_API_URL, params=self.param)
        if response.status_code == 200:
            return response.json()['items']
        else:
            return None


    def add_profession(self, value: str) -> None:
        """
        Adding the 'text' parameter to param
        :param value: string
        """
        self.param['text'] = value
        Vacancies.request_text = value

    def formated_data(self, data: list) -> list:
        """
        Data formatting
        :param data: list
        :return: list
        """
        work_data = []
        for item in data:
            match item['salary']['currency']:
                case 'USD':
                    if item['salary']['from'] is None:
                        salary = int(item['salary']['to']) * 100
                        salary_currency = 'руб'
                    else:
                        salary = item['salary']['from'] * 100
                        salary_currency = 'руб'
                case 'EUR':
                    if item['salary']['from'] is None:
                        salary = int(item['salary']['to']) * 107
                        salary_currency = 'руб'
                    else:
                        salary = item['salary']['from'] * 107
                        salary_currency = 'руб'
                case 'RUR':
                    if item['salary']['from'] is None:
                        salary = int(item['salary']['to'])
                        salary_currency = 'руб'
                    else:
                        salary = item['salary']['from']
                        salary_currency = 'руб'

            work_dict = {'name': item['name'],
                         'requirement': item['snippet']['requirement'],
                         'responsibility': item['snippet']['responsibility'],
                         'salary': salary,
                         'salary_currency': salary_currency,
                         'url': item['apply_alternate_url'],
                         'employer': item['employer']['name']
                         }
            work_data.append(work_dict)
        return work_data
