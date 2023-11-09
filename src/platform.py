


class HeadHunterAPI:
    def __init__(self, api_key):
        self.__api_key = api_key
        self.__hh = ('headhunter', 'v3', developerKey=self.__api_key)


    @poetry
    def api_key(self):
        return self.__api_key



class SuperJobAPI:
    pass