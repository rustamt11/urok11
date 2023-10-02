from django.db import models

class Student(models.Model):
    INSTRUMENT_CHOICES = [
        ('P', 'Piano'),
        ('G', 'Guitar'),
        ('V', 'Violin'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    course = models.PositiveIntegerField()
    instrument = models.CharField(max_length=1, choices=INSTRUMENT_CHOICES)
    average_score = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    has_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
