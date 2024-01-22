from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=70)
    gender = models.CharField(max_length=70)

    def __str__(self):
        return f'Booking: {self.name}'
    
    class Meta:
        ordering = ['id']
