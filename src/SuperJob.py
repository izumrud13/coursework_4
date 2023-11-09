from src.JobSearchService import JobSearchService
import requests


class SuperJobAPI(JobSearchService):

    def get_vacancies(self, search):
        """ Формирование запроса на SuperJob"""
        headers = {
            'X-Api-App-Id': "v3.r.137939262.2cdae9780058f951ba6d7ca739757cabfee656af"
                            ".7222c5992af77f3e8f94ce21882bbd3026de8c8f"
        }

        sj_request = requests.get(url="https://api.superjob.ru/2.0/vacancies/", headers=headers, params=search)
        if sj_request.status_code != 200:
            raise NameError(f"Удаленный сервер не отвечает {sj_request.status_code}")
        return sj_request.json()
