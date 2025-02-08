# File di funzioncine utili...
import datetime


def clean_string(value):
    s = str(value).strip()
    return s

def fstring(valore, lunghezza):
    l = len(str(valore))
    if l >= lunghezza:
        return lunghezza
    d = (lunghezza-l)
    s = ""
    for i in range(1, d):
        s += " "
    return str(valore)+s

def get_data_oggi():
    data = datetime.datetime.now()
    return data

def stringa_log_csv(op, dato, note=""):
    log = f"{get_data_oggi()};{op};{dato};{note}"
    return log
