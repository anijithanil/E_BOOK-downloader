from django.db import models

# Create your models here.
class FilesUpload(models.Model):
    name = models.CharField(max_length=100,null=True)
    desc = models.TextField(max_length=300,default='SOME STRING')
    image = models.ImageField(upload_to='bookimage',default='')
    file = models.FileField(upload_to='pdf')

    # def __str__(self):
    #     return self.name
