from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank= True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=20)
    summary     = models.TextField(default='this is cool')

    def get_absolute_url(self):
        # return f"/view/{self.id}/"  # There is better way of doing it
        return reverse("products:viewItem", kwargs= {"my_id": self.id})