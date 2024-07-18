from ast import Str
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default="Cra 3 # 12-99")
    id_card = models.IntegerField(blank=True,default=1234567890)
    phone = models.CharField(max_length=15)
    picture = models.ImageField(upload_to='users/pictures',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    country = models.CharField(max_length=100,default="COL")
    province = models.CharField(max_length=100,default="Monaco")
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField(blank=True,default="995577")
    date_birth = models.DateTimeField(default='2000-01-01',blank=True)
    favorites = models.CharField(max_length=200, default="", blank=True)
    
    def __str__(self) -> str:
        return self.user.username
    
    def addFavorite(self, number):
        myfavorites = list(self.favorites.split())
        if(number in myfavorites):
            pass
        else:
            myfavorites.append(number)
            strfavorite = " ".join(myfavorites)
            self.favorites = strfavorite
        
    def removeFavorite(self, number):
        myfavorites = list(self.favorites.split())
        if(number in myfavorites):
            myfavorites.remove(number)
            strfavorite = " ".join(myfavorites)
            self.favorites = strfavorite
        
        
    def getFavorites(self):
        return list(self.favorites.split())