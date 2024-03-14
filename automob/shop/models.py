from django.db import models

class Category(models.Model):
    name  = models.CharField(max_length=40)
    image = models.ImageField(upload_to='shop/categories',null=True,blank=True)


    def __str__(self):
        return self.name


class Part(models.Model):
    name = models.CharField(max_length=40)
    desc = models.TextField()
    image = models.ImageField(upload_to='shop/parts',null=True,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
