from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
  

# Create your models here.

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=60)
    phone_number = models.IntegerField(default=717878813)
    bio = models.TextField(default='')
    email = models.EmailField(max_length=60)

    def __str__(self):
        return self.user

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if not created:
#         Profile.objects.create(user=instance)
        

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, created, **kwargs):
#     instance.profile.save()


class Neighbor(models.Model):
    name =models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    health_contact = models.IntegerField( blank=True, default=+254717878813)
    police_contact = models.IntegerField( blank=True, default=999)
    occupants_count = models.IntegerField(default=1)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='neighbor')
    


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
    def search_business(cls, search_term):
        return cls.objects.filter(business_name__icontains=search_term).all()

class Post(models.Model):
    post_title = models.CharField(max_length=60)
    post_description = models.TextField(default='')
    posted = models.DateTimeField(auto_now_add=True)
    