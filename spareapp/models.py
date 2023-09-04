from django.db import models
from django.utils import timezone
#a model is a description of a physical database table.(a table is also called a relation)
#any database that stores data in a tabular format is called a relational database
# Create your models here
class Category(models.Model):
    name = models.CharField(max_length=50,null=False, blank=False)
    def __str__(self):
        return self.name 
    
      
class Product(models.Model):
    #referencing the catergory of the product.
    Category_name = models.ForeignKey(Category, on_delete = models.CASCADE, null=False, blank=False)
    item_name = models.CharField(max_length=50, null=False, blank=False)
    item_origin = models.CharField(max_length=50, null=False, blank=False)
    total_quantity = models.IntegerField(default=0, null=False, blank=False)
    issued_quantity = models.IntegerField(default=0, null=False, blank=False)
    recieved_quantity = models.IntegerField(default=0, null=False, blank=False)
    unit_price = models.IntegerField(default=0, null=False, blank=False)
    date_of_arrival = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.item_name

   
class Sale(models.Model):
    #referencing the category of the item
    item = models.ForeignKey(Product, on_delete= models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(default=0, null=False, blank=False)
    amount_recieved = models.IntegerField(default=0, null=False, blank=False)
    issued_to = models.CharField(max_length=50, null=False, blank=False)
    unit_price = models.IntegerField(default=0, null=False, blank=False)
    branch_name = models.CharField(max_length=50, null=False, blank=False)

    
    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)
    
    def get_change(self):
        change = self.get_total()-self.amount_recieved
        return abs(int(change))
    
    def __str__(self):
        return self.item.item_name 



