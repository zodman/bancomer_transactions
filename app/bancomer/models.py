from django.db import models

class Category(models.Model):
    name=models.CharField(max_lenght=40)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    description=models.CharField(max_lenght=100)
    amount=models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, 
                                 blank=True, null=True)
    applied =models.DateFIeld()
