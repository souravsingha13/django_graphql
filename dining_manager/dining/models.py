from django.db import models

class Consumer(models.Model):
    name = models.CharField(max_length= 200)
    email = models.CharField(max_length=200)
    image = models.FileField(blank=True, null=True,upload_to='customers/')

    def __str__(self) -> str:
        return self.name
    
class ProductCatagory(models.Model):
    name = models.CharField(max_length= 200)

    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    name = models.CharField(max_length= 200)
    catagory = models.ForeignKey(ProductCatagory, on_delete=models.CASCADE,  related_name="products")


    def __str__(self) -> str:
        return self.name
    
class Expenses(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE,  related_name="expences")
    quantity = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    buyer = models.ForeignKey(Consumer, on_delete= models.CASCADE, related_name='purchases')

