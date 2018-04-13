from django.db import models


class Picture(models.Model):
    TYPE_CHOICES = (
        ('Пейзаж', 'Пейзаж'),
        ('Натюрморт', 'Натюрморт'),
        ('Портрет', 'Портрет'),
        ('Ню', 'Ню'),
    )
    p_image = models.ImageField(verbose_name=u"Изображение:")
    p_name = models.CharField(max_length=200, verbose_name=u"Название:")
    p_type = models.CharField(max_length=40, choices=TYPE_CHOICES, verbose_name=u"Жанр:")
    p_width = models.CharField(max_length=15, verbose_name=u"Ширина:")
    p_height = models.CharField(max_length=15, verbose_name=u"Высота:")
    p_year = models.CharField(max_length=4, verbose_name=u"Год:")
    p_price = models.IntegerField(verbose_name=u"Цена:")
    p_in_stock = models.BooleanField(default=True, verbose_name=u"Жанр:")

    class Meta:
        verbose_name = "Картина"
        verbose_name_plural = "Картины"
        ordering = ['p_price']

    def __str__(self):
        return '%s' % self.p_name
