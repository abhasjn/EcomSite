from django.db import models

# Create your models here.
class Product(models.Model):
    # auto - incremental pk
    product_id = models.AutoField

    category=models.CharField(max_length=50, default="")
    subcategory=models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField( upload_to="shop/images", default="")


    ### by doing this , we will be able to see names in admin pannel for data
    def __str__(self):
        return self.product_name
    