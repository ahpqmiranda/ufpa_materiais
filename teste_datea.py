import locale
import datetime


def data_mes_extenso(data):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return data.strftime('%d de %B de %Y')


def formata_mes(data):
    locale.setlocale(locale.LC_TIME, "en_US.UTF-8")
    dt = datetime.datetime.strptime(data, '%B')
    locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
    return dt.strftime('%B').capitalize()


data = datetime.datetime.now()
print(data)
print(data_mes_extenso(data))
print(formata_mes('January'))
print(formata_mes('February'))
