from enum import Enum

token = "5528109695:AAGwHhlTVCUpsCAx2fbVoX5ltreiNOmDzzg"
db_file = "../database.vdb"

YES_LIST = ['да', 'конечно', 'ага', 'пожалуй']
NO_LIST = ['нет', 'нет, конечно', 'ноуп', 'найн']
RESULT_STATES = ["3", "4"]

FIRST_QUESTION = "Привет! Я могу отличить кота от хлеба. Объект перед тобой квадратный?"
SECOND_QUESTION = "У него есть уши?"
CAT_RESULT = "Это кот, а не хлеб, не ешь его!"
BREAD_RESULT = "Это хлеб, а не кот, ешь его!"
ERROR = "Я тебя не понял, ответь ещё раз, пожалуйста"
RESTART = "Если хочешь спросить меня ещё раз, введи команду /reset!"


class States(Enum):
    S_START = "0"
    S_FIRST_QUESTION = "1"
    S_SECOND_QUESTION = "2"
    S_CAT_RESULT = "3"
    S_BREAD_RESULT = "4"
