from django.db import models
from django.db.models.base import Model

# Create your models here.
#while creating models we should make class with arguments models.Model & defile different tables as per necessity
class Note(models.Model):
    title = models.CharField(max_length= 100)
    description = models.TextField()
    # string representation of model in database i.e it shows title and description instead of other randoms
    def __str__(self):
        return self.title, self.description