from django.db import models


class MySimpleModel(models.Model):
    col = models.BooleanField()

