import random

LOGIN = 'daahaaa@icloud.com'
PASSWORD = '_5Z4GUeDFwL5WAr'
BAD_PASSWORD = '12345'

INITIAL_URL = 'https://target.my.com/'
DASHBOARD_URL = 'https://target.my.com/dashboard'

random_surname = ['Chepigo', 'Ivanov', 'Sidorov', 'Petrov', 'Lebedev', 'Yakovlev']
random_name = ['Danya', 'Andrey', 'Sasha', 'Dima', 'Artyom', 'Lesha']
random_patronymic = ['Stanislavovich', 'Ivanovich', 'Sergeyevich', 'Alexeyevich']

NAME = random_surname[random.randint(0,5)] + ' ' + random_name[random.randint(0,5)] + ' ' + random_patronymic[random.randint(0,3)]
TELEPHONE = '8' + str(random.randint(1000000000, 9999999999))

STATISTIC_URL = 'https://target.my.com/statistics'
PRO_URL = 'https://target.my.com/pro'
