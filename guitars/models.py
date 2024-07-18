from email.mime import image
from django.db import models

# Create your models here.
class Brand(models.Model):
    id_brand = models.AutoField(primary_key=True)
    name_company = models.CharField(max_length=45)
    website_address = models.CharField(max_length=100)
    origin = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name_company

class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    name_category = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.name_category

class Model(models.Model):
    id_model = models.AutoField(primary_key=True)
    name_model = models.CharField(max_length=45)
    launch_year = models.IntegerField()
    number_copies = models.IntegerField()
    id_fk_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, db_column='id_fk_brand')

    def __str__(self) -> str:
        return self.name_model

class Guitar(models.Model):
    id_guitar = models.AutoField(primary_key=True)
    name_guitar = models.CharField(max_length=100)
    size = models.IntegerField()
    weight = models.IntegerField()
    color = models.CharField(max_length=45)
    material = models.CharField(max_length=45)
    date_sale = models.DateField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    favorite = models.BooleanField(blank=False, default=False)
    image = models.ImageField(null=True, blank=True,upload_to='guitars/static/guitars/images')
    id_fk_model = models.ForeignKey(Model, on_delete=models.CASCADE, db_column='id_fk_model')
    id_fk_category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='id_fk_category')

    def __str__(self) -> str:
        return self.name_guitar
    
    def specs(self):
        my_model = Model.objects.get(pk=self.id_fk_model.id_model)
        my_brand = Brand.objects.get(pk=my_model.id_fk_brand.id_brand)
        context = {
            "id_brand": my_brand.id_brand,
            "name_brand":my_brand.name_company,
            "id_model":my_model.id_model,
            "name_model":my_model.name_model,
        }
        return context
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class ImagesGuitar(models.Model):
    image = models.ImageField(null=True, blank=True,upload_to='guitars/static/guitars/images')
    id_fk_guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE, related_name='images')
    
    def __str__(self):
        name = self.guitar.name_guitar + ", ID image: " + str(self.pk)
        return name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url