from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class CustomerData(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    template = models.CharField(max_length=200, blank=True)
    customerName = models.CharField(max_length= 50)
    companyName = models.CharField(max_length= 100)
    aboutUsText = models.TextField(max_length= 500)
    image1 = models.ImageField(upload_to = "assets/images", null = False, blank = False, default="bild1")
    image2 = models.ImageField(upload_to = "assets/images", null = False, blank = False,  default="bild2")
    image3 = models.ImageField(upload_to = "assets/images", null = False, blank = False,  default="bild3")
    adress = models.CharField(max_length= 100)
    telephone = models.CharField(max_length= 15)
    email = models.EmailField(max_length= 255)
    def __str__(self):
        return self.customerName

