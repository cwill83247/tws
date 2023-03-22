from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Voucher(models.Model):
    code = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100)
    amountpercentage = models.IntegerField(validators=[MinValueValidator(0),
                                           MaxValueValidator(50)],
                                           help_text="Percentage 0%-50%")
    expiry_date = models.DateTimeField()

    def is_valid(self):
        return self.expiry_date > timezone.now()
