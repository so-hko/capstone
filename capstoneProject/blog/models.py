from django.db import models

class medicine(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=50)
    ingredient = models.CharField(max_length=300)
    effect = models.CharField(max_length=250)
    dosage = models.CharField(max_length=250)

    def __str__(self):
        return self.name
