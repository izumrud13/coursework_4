from src.HeadHunter import HeadHunterAPI

hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies()
print(hh_vacancies)