import csv

from parserapp.models import Item


def load_csv_file(filename):
    data_in_bd = []
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        read_csv = csv.DictReader(csvfile, delimiter=';')
        for row in read_csv:
            data_in_bd.append(Item(code=row.get('Код'),
                                   name=row.get('Наименование'),
                                   level_one=row.get('Уровень1'),
                                   level_two=row.get('Уровень2'),
                                   level_three=row.get('Уровень3'),
                                   price=int(row.get('Цена')) if row.get('Цена').strip() else 0,
                                   price_cp=int(row.get('ЦенаСП')) if row.get('ЦенаСП').strip() else 0,
                                   quantity=float(row.get('Количество')) if row.get('Количество').strip() else 0,
                                   properties=row.get('Поля свойств'),
                                   join_shopping=row.get('Совместные покупки'),
                                   measurement_unit=row.get('Единица измерения'),
                                   picture=row.get('Картинка'),
                                   is_view_main=int(row.get('Выводить на главной')),
                                   description=row.get('Описание')))

    return data_in_bd
