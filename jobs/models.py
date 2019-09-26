from django.db import models


class Job(models.Model):

    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)


    def __str__(self):
        x= self.summary.split()
        return x[0]+" "+x[1]



