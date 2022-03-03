from django.db import models


class Item(models.Model):
    code = models.CharField(max_length=48, verbose_name='Код')
    name = models.CharField(max_length=256, verbose_name='Наименование')
    level_one = models.CharField(max_length=48, blank=True, null=True, verbose_name='Уровень1')
    level_two = models.CharField(max_length=48, blank=True, null=True, verbose_name='Уровень2')
    level_three = models.CharField(max_length=48, blank=True, null=True, verbose_name='Уровень3')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    price_cp = models.PositiveIntegerField(default=0, verbose_name='ЦенаСП')
    quantity = models.FloatField(default=0, verbose_name='Количество')
    properties = models.TextField(verbose_name='Поля свойств', blank=True, null=True,)
    join_shopping = models.TextField(verbose_name='Совместная покупка', blank=True, null=True,)
    measurement_unit = models.CharField(max_length=15, verbose_name='Единица измерения')
    picture = models.ImageField(upload_to='image_item', verbose_name='Картинка', blank=True, null=True,)
    is_view_main = models.BooleanField(default=False, verbose_name='Вывод на главной')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class CSV_file(models.Model):
    file = models.FileField(upload_to='CSV_files', verbose_name='CSV_файл')

    class Meta:
        verbose_name = 'CSV_файл'
        verbose_name_plural = 'CSV_файлы'

    def __str__(self):
        return self.file.name
