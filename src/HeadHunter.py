from src.JobSearchService import JobSearchService
import requests


class HeadHunterAPI(JobSearchService):

    def get_vacancies(self, search):
        """
        Формирование запроса на HeadHunter
        """
        headers = {
            'User-Agent': "HOK4D472UKH0PTF1DTHSK9FF36529Q4K9VPOSJB9BJM2MPT39MF3GJJNUE9PJDPT"
        }
        hh_request = requests.get(url=f"https://api.hh.ru/vacancies", headers=headers, params=search)
        if hh_request.status_code != 200:
            raise NameError(f"Удаленный сервер не отвечает {hh_request.status_code}")
        return hh_request.json()
