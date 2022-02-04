from django.db import models


# Create your models here.


class table_test(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    birth = models.DateField()
    hobby = models.CharField(max_length=30)

    def __str__(self):
        return "%s  %s  %s  %s" % (self.id, self.name, self.birth, self.hobby)

    class Meta:
        db_table = "table_test"
