from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class person(models.Model):
    registerno = models.CharField(null=True, max_length=15)
    father_registerno = models.CharField(null=True, max_length=15)
    first_name = models.CharField(max_length=15, default="")
    last_name = models.CharField(max_length=15, default="")
    sername = models.CharField(max_length=15, default="")
    g_father = models.CharField(max_length=15, default="")
    qualification = models.CharField(max_length=15, default="")
    email = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=200, default="")
    phone = models.CharField(max_length=15, default="")
    image = models.ImageField(upload_to="upload/", default="")


    def __str__(self):
        return self.first_name

