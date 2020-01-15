from django.db import models



class Category(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    description=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, 
                                 blank=True, null=True)
    applied =models.DateField()


    class Meta:
        unique_together  = ("applied", "description", "amount")
        ordering = ("applied",)


class Summary(Transaction):
    class Meta:
        proxy = True
        verbose_name = "Summary"
        verbose_name_plural = "Summary"


