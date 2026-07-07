from django.db import models

class Education(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('Ongoing', 'Ongoing'),
    ]   
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    start_date = models.CharField(max_length=7) 
    end_date = models.CharField(max_length=7, null=True, blank=True) 
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution}"