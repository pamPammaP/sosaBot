from datetime import datetime
from random import randint


def get_time():

    """if datetime.now().hour < 22 and 9 < datetime.now().hour:
        hourstime = randint(datetime.now().hour, 22)
        daytime = datetime.now().day
    else:"""
    hourstime = randint(9, 22)
    daytime = datetime.now().day + 1
    minutstime = randint(0, 59)
    secundstime = randint(0, 59)
    timesos = datetime(datetime.now().year, 
                        datetime.now().month,
                        daytime,
                        hourstime, 
                        minutstime,
                        secundstime)
    return timesos.strftime("%d-%H-%M")

def get_com():
    with open('commentSos.txt', 'r') as f:
        print(f.readlines())
