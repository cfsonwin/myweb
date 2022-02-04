from django.db import models
from datetime import datetime
# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField(null=True, default=18)
    phone = models.CharField(max_length=16)
    addtime = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "mymodel_users"
