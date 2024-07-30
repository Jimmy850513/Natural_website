from django.db import models


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=200,null=False)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True)
    quantity = models.IntegerField(null=True)
    status = models.CharField(max_length=10,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_id},{self.item_name}"
    class Meta:
        db_table = "Items"

class Item_Status(models.Model):
    item_status_no = models.CharField(unique=True,max_length=10,null=False)
    item_status_name = models.CharField(unique=True,max_length=50,null=False)

    def __str__(self):
        return f"{self.item_status_no}:{self.item_status_name}"
    
    class Meta:
        db_table = 'Item_Status'