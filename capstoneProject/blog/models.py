from django.db import models

class OTCInfo(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    ingredients = models.CharField(max_length=255)
    effect = models.TextField()
    dosage = models.TextField()
    caution = models.TextField(null=True)
    nation = models.CharField(max_length=10)
    image = models.ImageField(
            blank=True,
            upload_to="otc_image"
            )

    def __str__(self):
        return self.name


class ETCInfo(models.Model):
    name = models.CharField(max_length=255,primary_key=True)
    ingredients = models.CharField(max_length=255)
    effect = models.TextField()
    dosage = models.TextField()
    caution = models.TextField(null=True)
    nation = models.CharField(max_length=5)
    image = models.ImageField(
            blank=True,
            upload_to="ect_image"
            )

    def __str__(self):
        return self.name


class Pill(models.Model):
    name = models.CharField(max_length=255,primary_key=True)
    maker = models.CharField(max_length=20)
    shape = models.CharField(max_length=10)
    fcolor = models.CharField(max_length=10, null=True, blank=True)
    bcolor = models.CharField(max_length=10, null=True, blank=True)
    fmark = models.CharField(max_length=20, null=True, blank=True)
    bmark = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(
            blank=True,
            upload_to="pill_image"
            )

    def __str__(self):
        return self.name

class Photo(models.Model):
    post = models.ForeignKey(OTCInfo, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

