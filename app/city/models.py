from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name="نام")
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = "استان"
        verbose_name_plural = "استان ها"


class City(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name = "استان")
    name = models.CharField(max_length=256, unique=True, verbose_name="نام")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "شهر"
        verbose_name_plural = "شهر ها"




