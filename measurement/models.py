from django.db import models

class Sensor(models.Model):
    sensor_name = models.CharField(max_length=100, verbose_name='Датчик')
    description = models.CharField(max_length=100, default=None, verbose_name='Описание')

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='sensor', on_delete=models.CASCADE)
    temperature = models.FloatField(verbose_name='Показания температуры датчика')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время передачи показаний датчика')
    image = models.ImageField(max_length=100, null=True, verbose_name='Фото объекта')
