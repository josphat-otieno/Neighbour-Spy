from django.db import models
#  

# Create your models here.

class Neighbor(models.Model):
    name =models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    occupants_count = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class User (models.Model):
    user_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    neighborhood = models.ForeignKey(Neighbor, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name

class Business (models.Model):
    business_name=models.CharField(max_length=60)
    business_email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighbor, on_delete=models.CASCADE)


    def __str__(self):
        return self.business_name
