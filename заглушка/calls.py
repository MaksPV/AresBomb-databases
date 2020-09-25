# import requests

class Calls(object):
    
    all = 0
    author = "База заглушка"
    
    def __init__(self):
        pass

    def send(self, serv, phone):
        print("Звонки не работают")
        raise                
        # if serv == 0: requests.get('https://findclone.ru/register', params={'phone': '+' + phone})
        # else: print("Ошибка сервиса")