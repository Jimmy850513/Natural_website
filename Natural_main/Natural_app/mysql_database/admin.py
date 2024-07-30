from django.db import models

class Admin_User(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.CharField(null=False,unique=True,max_length=50)
    password = models.CharField(null=False,max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id},{self.account}"
    
    class Meta:
        db_table = 'Admin'