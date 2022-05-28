from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "employee"



