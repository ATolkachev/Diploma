from django.db import models

class Date(models.Model):
    date_value = models.DateField('Дата')

    def __str__(self):
        return self.date_value

class Country(models.Model):
    country_code = models.CharField('Код страны', max_length = 4)

    def __str__(self):
        return self.country_code

class Data(models.Model):
    date_value = models.ForeignKey(Date, on_delete = models.CASCADE)
    country_code = models.ForeignKey(Country, on_delete = models.CASCADE)
    confirmed = models.IntegerField('Подтвержденные случаи')
    deaths = models.IntegerField('Количество смертей')
    stringency_actual = models.IntegerField('Актуальный уровень ограничений')
    stringency = models.IntegerField('Уровень ограничений')

    def __str__(self):
        return self.deaths


