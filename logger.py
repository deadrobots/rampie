import logging
from time import strftime
import constants as c
from wallaby import seconds

def log(message, filename="general.log"):
        datetime = strftime("%Y-%m-%d %H:%M:%S")
        dt = seconds() - c.startTime
        FORMAT = '%(datetime)s %(dt)s: %(message)s'
        logging.basicConfig(filename=filename, format=FORMAT)
        data = {'dt':dt, 'datetime':datetime}
        # print(str(data) + " " + message)
        logging.warning(message, extra=data)

def data_log(message, filename="general.log"):
        dt = seconds() - c.startTime
        FORMAT = '%(dt)s\t%(message)s'
        logging.basicConfig(filename=filename, format=FORMAT)
        data = {'dt':dt}
        # print(str(data) + " " + message)
        logging.warning(message, extra=data)
