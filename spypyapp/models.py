from django.db import models
from django.contrib.auth.models import User
  

# Create your models here.

class Neighbor(models.Model):
    name =models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    health_contact = models.IntegerField( blank=True, default=+254717878813)
    police_contact = models.IntegerField( blank=True, default=999)
    occupants_count = models.IntegerField(default=1)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.name

    def create(self):
        self.save()

    def delete_neighbour(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        neighborhood = cls.objects.get(id = neighborhood_id)
        return neighborhood

    @classmethod
    def update_neighborhood(cls, neighborhood_id):
        neighborhood  = cls.objects.filter(id=neighborhood_id).update()
        return neighborhood

    @classmethod
    def update_count(cls, count):
        neighborhood_count = cls.objects.filter(occupants_count=1).update(occupants_count=count)
        return neighborhood_count


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=60)
    bio = models.TextField(default='')
    email = models.EmailField(max_length=60)
    neighbourhood = models.ForeignKey(Neighbor, on_delete=models.SET_NULL, null=True, related_name='users', blank=True)

  


    def __str__(self):
        return self.user_name

class Business (models.Model):
    business_name=models.CharField(max_length=60)
    business_description = models.TextField(default='')
    business_email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighbor, on_delete=models.CASCADE)


    def __str__(self):
        return self.business_name

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, business_name):
        business = cls.objects.filter(business_name__icontains=business_name).all()
        return business
