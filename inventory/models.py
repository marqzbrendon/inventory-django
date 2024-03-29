from django.db import models

class Sessions(models.Model):
    user_code = models.CharField(max_length=20, unique=True)
    user = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return f"{self.user} | {self.user_code}"

class Item(models.Model):
    item = models.CharField(max_length=25)
    quantity = models.IntegerField()
    user_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"