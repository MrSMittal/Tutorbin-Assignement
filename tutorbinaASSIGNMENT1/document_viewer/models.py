from django.db import models
import datetime
# Create your models here

class Grouping(models.Model):
    grouptitle=models.CharField(max_length=200,default="N/A")
    createddate=models.DateField(default=datetime.date.today)

class DocumentUploader(models.Model):
    title=models.CharField(max_length=200)
    file=models.FileField(upload_to='documents/')
    created_at=models.DateField(default=datetime.date.today)
    group_id=models.ForeignKey(Grouping, on_delete=models.CASCADE)

