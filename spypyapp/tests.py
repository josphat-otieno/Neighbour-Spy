from django.db.models.query_utils import select_related_descend
from django.test import TestCase
from .models import *

# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User(username='jose', password = 'joseotis45')
        self.user.save()
        self.profile = Profile(user_name='jose', phone_number=7171878813, bio= 'okay', email= 'jose@gmail.com', user = self.user)
        self.profile.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))


class NeighbourTestCase(TestCase):
    def setUp(self):
        self.user = User(username='jose', password = 'joseotis45')
        self.user.save()
        self.profile = Profile(user_name='jose', phone_number=7171878813, bio= 'okay', email= 'jose@gmail.com', user = self.user)
        self.profile.save()

        self.new_neighbour = Neighbor(name='jose', location='nairobi',health_contact=7171878813,police_contact=7171878813,occupnats_count=1, profile = self.profile  )
        self.new_neighbour.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighbour, Neighbor))

    def test_save(self):
        self.new_neighbour.create()
        neighbors= Neighbor.objects.all()
        self.assertTrue(len(neighbors)>0)

    def test_delete(self):
        self.new_neighbour.create()
        neighbors= Neighbor.objects.all()
        self.new_neighbour.delete()
        self.assertTrue(len(neighbors)==0)

    def test_find_neighbour_by_id(self):
        neighbor = self.new_neighbour.find_neighborhood(self.new_neighbour.id)
        neighbors = Neighbor.objects.filter(id=self.new_neighbour.id)
        self.assertTrue(neighbor, neighbors)
       
    def test_update_neighbourhood(self):
        self.new_neighbour.create()
        self.new_neighbour.update_neighborhood(self.new_neighbour.id, 'name')
        neighbor_updated = Neighbor.objects.filter(name= 'name')
        self.new_neighbour.create()
        self.assertTrue(neighbor_updated,Neighbor )

class BusinessTest(TestCase):
    def setUp(self):
        self.user = User(username='jose', password = 'joseotis45')
        self.user.save()
        self.profile = Profile(user_name='jose', phone_number=7171878813, bio= 'okay', email= 'jose@gmail.com', user = self.user)
        self.profile.save()

        self.new_neighbour = Neighbor(name='jose', location='nairobi',health_contact=7171878813,police_contact=7171878813,occupnats_count=1, profile = self.profile  )
        self.new_neighbour.save()

        self.new_business= Business(business_name = 'mutura', business_description='nyamu chom', business_email = 'bus@gmail.com', neighbor = self.new_neighbour)
        self.new_business.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business, Business))

    def test_save_method(self):
        self.new_business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business)>0)

    def test_delete_method(self):
        self.new_business.save_business()
        business = Business.objects.all()
        self.new_business.delete_business()
        self.assertTrue(len(business)==0)

    def test_search_business(self):
        self.new_business.save_business()
        found_business = self.new_business.search_business(search_term='business')
        self.assertTrue(len(found_business)==1)
        

class PostTestCase(TestCase):
    def setUp(self):
        self.new_post = Post(post_title = 'job', post_description='joy')
        self.new_post.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))



        




