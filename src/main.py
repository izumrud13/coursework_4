from src.HeadHunter import HeadHunterAPI
from src.SuperJob import SuperJobAPI
from src.json_file import InfoSaver
from src.vacancies import Vacancies


class ForUser:
    """
    User Interaction Class
    """
    def __init__(self):
        self.hh_api = HeadHunterAPI()
        self.sj_api = SuperJobAPI()

    def start_loop(self) -> None:
        """
        Start menu
        """
        while True:
            print('-' * 50)
            print('Greetings! This application will help you find a job.')
            print('Command menu:')
            print('0. Exit.')
            print('1. Search for vacancies on the HeadHunter platform.')
            print('2. Search for vacancies on the SuperJob platform.')
            print()
            choice = input('Enter the command: ')
            match choice:
                case '0':
                    print()
                    print('Goodbye.')
                    quit()
                case '1':
                    print('-' * 50)
                    hh_choice = 'hh'
                    self.choice_profession(hh_choice)
                case '2':
                    print('-' * 50)
                    sj_choice = 'sj'
                    self.choice_profession(sj_choice)
                case _:
                    print('-' * 50)
                    print('Unknown command.')

    def choice_profession(self, value: str) -> None:
        """
        Request a profession from the user
        :param value: string with rofession
        """
        while True:
            print('Command menu:')
            print('0. Exit.')
            print('1. Back to previous menu.')
            user_input = input('Enter a profession or available command: ').lower().strip()
            match user_input:
                case '0':
                    print('Goodbye.')
                    quit()
                case '1':
                    return
                case _:
                    if value == 'hh':
                        self.hh_api.add_profession(user_input)
                        self.average_loop(value)
                    if value == 'sj':
                        self.sj_api.add_profession(user_input)
                        self.average_loop(value)

    def average_loop(self, value: str) -> None:
        """
        Output processing average menu for vacancies
        """
        while True:
            print('-' * 50)
            print('Command menu:')
            print('0: Exit.')
            print('1: Show all vacancies.')
            print('2: Show top 10 vacancies by salary.')
            print('3: Return to previous menu.')
            user_input = input('Enter the command: ')
            match user_input:
                case '0':
                    print('Goodbye.')
                    quit()
                case '1':
                    if value == 'hh':
                        print('-' * 50)
                        hh_data = self.hh_api.get_vacancies()
                        if hh_data is None:
                            print('Error receiving data')
                            return
                        hh_work_data = self.hh_api.formated_data(hh_data)
                        self.get_all_vacancies(hh_work_data)
                    if value == 'sj':
                        print('-' * 50)
                        sj_data = self.sj_api.get_vacancies()
                        if sj_data is None:
                            print('Error receiving data')
                            return
                        sj_work_data = self.sj_api.formated_data(sj_data)
                        self.get_all_vacancies(sj_work_data)
                case '2':
                    if value == 'hh':
                        print('-' * 50)
                        hh_data = self.hh_api.get_vacancies()
                        if hh_data is None:
                            print('Error receiving data')
                            return
                        hh_work_data = self.hh_api.formated_data(hh_data)
                        sorted_data = sorted(hh_work_data, key=lambda x: x['salary'], reverse=True)
                        self.get_top_10_by_salary(sorted_data)
                    if value == 'sj':
                        print('-' * 50)
                        sj_data = self.sj_api.get_vacancies()
                        if sj_data is None:
                            print('Error receiving data')
                            return
                        sj_work_data = self.sj_api.formated_data(sj_data)
                        sorted_data = sorted(sj_work_data, key=lambda x: x['salary'], reverse=True)
                        self.get_top_10_by_salary(sorted_data)
                case '3':
                    Vacancies.clear_vacancies_list()
                    print('-' * 50)
                    return
                case _:
                    print('-' * 50)
                    print('Unknown command.')

    def get_all_vacancies(self, data):
        """
        Output of all found vacancies
        """
        for part in data:
            Vacancies(part)
        work_list = Vacancies.all_vacancies
        for index in range(len(work_list)):
            print(f'Vacancy № {index + 1}.')
            work_list[index].get_info()
        self.last_loop(work_list)

    def get_top_10_by_salary(self, data):
        """
        Display of the first 10 vacancies by salary
        """
        for part in data[:10]:
            Vacancies(part)
        work_list = Vacancies.all_vacancies
        for index in range(len(work_list)):
            print(f'Vacancy № {index + 1}.')
            work_list[index].get_info()
        self.last_loop(work_list)

    def last_loop(self, data):
        """
        The last command menu
        """
        while True:
            print('-' * 50)
            print(f'{len(data)} vacancies shown upon request "{Vacancies.request_string.title()}".')
            print()
            print('Command menu:')
            print('0: Exit without saving data.')
            print('1: Saving data.')
            print('2: Starting a new search.')
            user_input = input('Enter the command: ')
            match user_input:
                case '0':
                    print('Goodbye.')
                    quit()
                case '1':
                    data = Vacancies.reformat_data()
                    saver = InfoSaver()
                    try:
                        saver.file_saving(data)
                        print('Data saved successfully.')
                        print()
                        print('Goodbye.')
                        quit()
                    except FileNotFoundError:
                        print('Wrong way to file')
                        continue
                case '2':
                    Vacancies.clear_vacancies_list()
                    self.start_loop()
                case _:
                    print('-' * 50)
                    print('Unknown command.')


if __name__ == '__main__':
    start = ForUser()
    start.start_loop()
